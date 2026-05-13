import asyncio
import signal

from aiohttp import web

from aiogram import Bot, Dispatcher

from src.config import AI_SERVICE_URL, BOT_TOKEN
from src.hotloader import auto_discover, init as init_hotloader
from src.handlers.callback import router as callback_router
from src.handlers.chat import router as chat_router
from src.handlers.mcps import router as mcps_router
from src.handlers.models import router as models_router
from src.handlers.ping import router as ping_router
from src.handlers.skill import router as skill_router
from src.handlers.start import router as start_router


async def health_check(request: web.Request) -> web.Response:
    return web.json_response({"status": "ok"})


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start_router, ping_router, skill_router, mcps_router, models_router, chat_router, callback_router)
    init_hotloader(bot, dp)
    auto_discover()

    app = web.Application()
    app.router.add_get("/health", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)

    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, stop_event.set)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(site.start())
        tg.create_task(dp.start_polling(bot))

        await stop_event.wait()

        tg.cancel_gracefully()


if __name__ == "__main__":
    asyncio.run(main())
