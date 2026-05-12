import asyncio
import os
import resource
import shutil
import tempfile
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Sandbox")

SANDBOX_TIMEOUT = int(os.environ.get("SANDBOX_TIMEOUT", "60"))
SANDBOX_MAX_OUTPUT = 1_000_000
SANDBOX_TTL = timedelta(minutes=10)
MAX_INSTANCES = 100
MAX_FILES_PER_WRITE = 10
MAX_FILE_SIZE = 1_048_576  # 1 MB
MAX_FILENAME_LEN = 256

RUNTIMES: dict[str, list[str]] = {
    "python": ["python3", "-c"],
    "py": ["python3", "-c"],
}


@dataclass
class SandboxInstance:
    sandbox_id: str
    dir: Path
    created_at: datetime
    timeout_seconds: int


_instances: dict[str, SandboxInstance] = {}


class CreateRequest(BaseModel):
    timeout: int = Field(default=SANDBOX_TIMEOUT, ge=1)


class CreateResponse(BaseModel):
    sandbox_id: str


class RunRequest(BaseModel):
    sandbox_id: str
    cmd: str
    args: list[str] = []
    cwd: str | None = None
    env: dict[str, str] = {}
    sudo: bool = False  # reserved, not used


class RunResponse(BaseModel):
    exit_code: int
    stdout: str
    stderr: str
    timed_out: bool


class ReadRequest(BaseModel):
    sandbox_id: str
    path: str


class ReadResponse(BaseModel):
    data: str | None


class WriteFileEntry(BaseModel):
    path: str = Field(max_length=MAX_FILENAME_LEN)
    content: str = Field(max_length=MAX_FILE_SIZE)


class WriteRequest(BaseModel):
    sandbox_id: str
    files: list[WriteFileEntry]


def _set_limits(timeout: int) -> None:
    resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout + 5))
    resource.setrlimit(resource.RLIMIT_FSIZE, (SANDBOX_MAX_OUTPUT, SANDBOX_MAX_OUTPUT))
    resource.setrlimit(resource.RLIMIT_NPROC, (64, 64))
    resource.setrlimit(resource.RLIMIT_NOFILE, (32, 32))
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))


def _safe_resolve(base: Path, user_path: str) -> Path:
    resolved = (base / user_path).resolve()
    if not str(resolved).startswith(str(base.resolve())):
        raise HTTPException(403, f"path escapes sandbox: {user_path}")
    return resolved


def _get_sandbox(sandbox_id: str) -> SandboxInstance:
    sb = _instances.get(sandbox_id)
    if not sb:
        raise HTTPException(404, f"Sandbox {sandbox_id} not found")
    return sb


@app.on_event("startup")
async def _cleanup_loop() -> None:
    async def _cleanup() -> None:
        while True:
            now = datetime.now()
            expired = [sid for sid, sb in _instances.items()
                       if now - sb.created_at > SANDBOX_TTL]
            for sid in expired:
                sb = _instances.pop(sid, None)
                if sb:
                    shutil.rmtree(sb.dir, ignore_errors=True)
            await asyncio.sleep(60)
    asyncio.create_task(_cleanup())


@app.post("/create", response_model=CreateResponse)
async def create_sandbox(req: CreateRequest) -> CreateResponse:
    if len(_instances) >= MAX_INSTANCES:
        raise HTTPException(503, "max instances reached, try again later")
    sandbox_id = uuid.uuid4().hex[:16]
    work_dir = Path(tempfile.mkdtemp(prefix="sandbox_"))
    _instances[sandbox_id] = SandboxInstance(
        sandbox_id=sandbox_id,
        dir=work_dir,
        created_at=datetime.now(),
        timeout_seconds=min(req.timeout, SANDBOX_TIMEOUT),
    )
    return CreateResponse(sandbox_id=sandbox_id)


@app.post("/run", response_model=RunResponse)
async def run_command(req: RunRequest) -> RunResponse:
    sb = _get_sandbox(req.sandbox_id)

    runtime = RUNTIMES.get(req.cmd)
    if runtime is None:
        raise HTTPException(400, f"unsupported runtime: {req.cmd}")

    if req.sudo:
        raise HTTPException(403, "sudo not allowed")

    safe_cwd = str(_safe_resolve(sb.dir, req.cwd or "")) if req.cwd else str(sb.dir)

    proc = await asyncio.create_subprocess_exec(
        *runtime,
        *req.args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=safe_cwd,
        preexec_fn=lambda: _set_limits(sb.timeout_seconds),
        env={**req.env, "PATH": "/usr/local/bin:/usr/bin:/bin"},
    )

    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(), timeout=sb.timeout_seconds
        )
        timed_out = False
    except asyncio.TimeoutError:
        proc.kill()
        stdout, stderr = await proc.communicate()
        timed_out = True

    return RunResponse(
        exit_code=proc.returncode if not timed_out else -1,
        stdout=stdout.decode(errors="replace")[:SANDBOX_MAX_OUTPUT],
        stderr=stderr.decode(errors="replace")[:SANDBOX_MAX_OUTPUT],
        timed_out=timed_out,
    )


@app.post("/read", response_model=ReadResponse)
async def read_file(req: ReadRequest) -> ReadResponse:
    sb = _get_sandbox(req.sandbox_id)
    path = _safe_resolve(sb.dir, req.path)
    if not path.exists() or not path.is_file():
        return ReadResponse(data=None)
    return ReadResponse(data=path.read_text(errors="replace"))


@app.post("/write")
async def write_files(req: WriteRequest) -> dict[str, bool]:
    sb = _get_sandbox(req.sandbox_id)
    if len(req.files) > MAX_FILES_PER_WRITE:
        raise HTTPException(413, f"max {MAX_FILES_PER_WRITE} files per write request")
    for f in req.files:
        path = _safe_resolve(sb.dir, f.path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f.content)
    return {"ok": True}


@app.post("/stop/{sandbox_id}")
async def stop_sandbox(sandbox_id: str) -> dict[str, bool]:
    sb = _get_sandbox(sandbox_id)
    shutil.rmtree(sb.dir, ignore_errors=True)
    _instances.pop(sandbox_id, None)
    return {"ok": True}
