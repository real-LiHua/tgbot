import os

import httpx

SANDBOX_URL = os.environ.get("SANDBOX_URL", "http://localhost:8080")


class SandboxClient:
    def __init__(self, sandbox_id: str, http: httpx.AsyncClient) -> None:
        self.sandbox_id = sandbox_id
        self._http = http

    @property
    def _run_url(self) -> str:
        return f"{SANDBOX_URL}/run"

    @property
    def _read_url(self) -> str:
        return f"{SANDBOX_URL}/read"

    @property
    def _write_url(self) -> str:
        return f"{SANDBOX_URL}/write"

    @property
    def _stop_url(self) -> str:
        return f"{SANDBOX_URL}/stop/{self.sandbox_id}"

    async def run_command(
        self,
        cmd: str,
        args: list[str] | None = None,
        *,
        cwd: str | None = None,
        env: dict[str, str] | None = None,
    ) -> dict:
        resp = await self._http.post(
            self._run_url,
            json={
                "sandbox_id": self.sandbox_id,
                "cmd": cmd,
                "args": args or [],
                "cwd": cwd,
                "env": env or {},
            },
            timeout=120,
        )
        resp.raise_for_status()
        return resp.json()

    async def read_file(self, path: str) -> str | None:
        resp = await self._http.post(
            self._read_url,
            json={"sandbox_id": self.sandbox_id, "path": path},
        )
        resp.raise_for_status()
        data = resp.json()
        return data["data"]

    async def write_files(self, files: list[dict]) -> None:
        resp = await self._http.post(
            self._write_url,
            json={"sandbox_id": self.sandbox_id, "files": files},
        )
        resp.raise_for_status()

    async def stop(self) -> None:
        try:
            await self._http.post(self._stop_url)
        except httpx.HTTPError:
            pass

    async def close(self) -> None:
        await self._http.aclose()

    @staticmethod
    async def create(*, timeout: int = 60) -> "SandboxClient":
        http = httpx.AsyncClient()
        resp = await http.post(
            f"{SANDBOX_URL}/create",
            json={"timeout": timeout},
        )
        resp.raise_for_status()
        sandbox_id = resp.json()["sandbox_id"]
        return SandboxClient(sandbox_id, http)
