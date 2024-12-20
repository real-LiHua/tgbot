from argparse import ArgumentParser

from telethon.events import NewMessage

parser = ArgumentParser("telegramctl", add_help=False, exit_on_error=False)
parser.add_argument("--promote", nargs="+", help="提权", metavar=("用户ID", "权限"))
parser.add_argument("--demote", nargs="+", help="降权", metavar=("用户ID", "权限"))
parser.add_argument("--mute", action="append", help="静言", metavar="用户ID[:持续时间]")
parser.add_argument("--unmute", action="append", help="解除静言", metavar="用户ID")
parser.add_argument("--kick", action="append", help="踢出", metavar="用户ID")
parser.add_argument("--ban", action="append", help="封禁", metavar="用户ID[:持续时间]")
parser.add_argument("--unban", action="append", help="解除封禁", metavar="用户ID")


async def callback(command: str, event: NewMessage.Event | None = None):
    args = parser.parse_args(command.split(" "))
    if args.ban:
        for item in args.ban:
            user, *time = item.split(":")
            time = time[0] if time else None
            print(user, time)


if __name__ == "__main__":
    import asyncio
    import sys

    parser.print_help()
    asyncio.run(callback(" ".join(sys.argv[1:])))
