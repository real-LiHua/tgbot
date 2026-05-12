import argparse

import httpx
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.formatting import Bold, Code, as_list

router = Router(name="skill")

API = "https://skills.sh/api/v1"

_parser = argparse.ArgumentParser(prog="/skill", description="Agent 技能管理")
_sub = _parser.add_subparsers(dest="cmd")

p = _sub.add_parser("find", help="搜索技能")
p.add_argument("query", help="搜索关键词")

p = _sub.add_parser("info", help="查看技能详情")
p.add_argument("skill_id", help="技能 ID (source/slug)")

p = _sub.add_parser("add", help="获取技能内容")
p.add_argument("skill_id", help="技能 ID (source/slug)")

_sub.add_parser("list", help="热门技能排行榜")

p = _sub.add_parser("init", help="创建技能模板")
p.add_argument("name", help="技能名称")


@router.message(Command("skill"))
async def handle_skill(message: types.Message) -> None:
    raw = message.text.removeprefix("/skill").strip()
    argv = raw.split() if raw else ["--help"]
    try:
        ns = _parser.parse_args(argv)
    except (SystemExit, argparse.Error):
        await message.answer(_parser.format_help())
        return

    match ns.cmd:
        case "find":
            await _find(message, ns.query)
        case "info":
            await _info(message, ns.skill_id)
        case "add":
            await _add(message, ns.skill_id)
        case "list":
            await _list(message)
        case "init":
            await _init(message, ns.name)


async def _find(message: types.Message, query: str) -> None:
    async with httpx.AsyncClient() as c:
        resp = await c.get(f"{API}/skills/search", params={"q": query, "limit": 10}, timeout=10)
    if resp.status_code != 200:
        await message.answer("搜索失败，请稍后重试。")
        return
    data = resp.json()
    skills = data.get("data", [])
    if not skills:
        await message.answer(f"未找到与 \"{query}\" 相关的技能。")
        return
    lines = [Bold(f"找到 {data.get('count', len(skills))} 个技能:\n")]
    for s in skills[:10]:
        lines.append(f"  {Code(s['id'])}  — {s['name']} ({s.get('installs', 0):,})")
    lines.extend(["", "使用 /skill info <id> 查看详情"])
    await message.answer(**as_list(*lines).as_kwargs())


async def _info(message: types.Message, skill_id: str) -> None:
    async with httpx.AsyncClient() as c:
        resp = await c.get(f"{API}/skills/{skill_id}", timeout=10)
    if resp.status_code == 404:
        await message.answer(f"未找到技能 \"{skill_id}\"。")
        return
    if resp.status_code != 200:
        await message.answer("获取详情失败，请稍后重试。")
        return
    data = resp.json()
    lines = [f"📦 {data.get('name', skill_id)}", f"  来源: {data.get('source', '')}", f"  安装: {data.get('installs', 0):,}"]
    for f in data.get("files") or []:
        if f["path"].lower() == "skill.md":
            lines.extend(["", "── SKILL.md ──", f.get("contents", "")[:3500]])
            break
    await message.answer("\n".join(lines)[:4096])


async def _add(message: types.Message, skill_id: str) -> None:
    async with httpx.AsyncClient() as c:
        resp = await c.get(f"{API}/skills/{skill_id}", timeout=10)
    if resp.status_code == 404:
        await message.answer(f"未找到技能 \"{skill_id}\"。")
        return
    if resp.status_code != 200:
        await message.answer("获取技能失败，请稍后重试。")
        return
    data = resp.json()
    skill_md = next((f["contents"] for f in data.get("files") or [] if f["path"].lower() == "skill.md"), None)
    if not skill_md:
        await message.answer(f"技能 {skill_id} 没有 SKILL.md 内容。")
        return
    await message.answer(
        f"已获取技能: {data.get('name', skill_id)}\n"
        f"来源: {data.get('source', '')}\n"
        f"安装量: {data.get('installs', 0):,}\n\n"
        f"```markdown\n{skill_md[:3500]}\n```"
    )


async def _list(message: types.Message) -> None:
    async with httpx.AsyncClient() as c:
        resp = await c.get(f"{API}/skills", params={"view": "all-time", "per_page": 15}, timeout=10)
    if resp.status_code != 200:
        await message.answer("获取列表失败，请稍后重试。")
        return
    skills = resp.json().get("data", [])
    if not skills:
        await message.answer("暂无技能数据。")
        return
    lines = [Bold("🏆 热门技能排行榜:\n")]
    for i, s in enumerate(skills[:15]):
        lines.append(f"  {i+1}. {Code(s['id'])}  — {s.get('installs', 0):,}")
    lines.extend(["", "详情: /skill info <id>"])
    await message.answer(**as_list(*lines).as_kwargs())


async def _init(message: types.Message, name: str) -> None:
    template = (
        f"---\nname: {name}\ndescription: 描述 {name} 的作用\n---\n\n"
        f"# {name}\n\n## 概述\n\n在这里描述这个技能的用途和使用场景。\n\n"
        f"## 使用方式\n\n描述如何触发和使用这个技能。\n\n## 示例\n\n```\n示例代码或用法\n```\n"
    )
    await message.answer(
        f"技能 \"{name}\" 模板已生成:\n\n```markdown\n{template}\n```\n\n"
        f"将其保存为 SKILL.md 并发布到 GitHub 仓库即可分享。"
    )
