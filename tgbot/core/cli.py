from argparse import ArgumentParser

parser = ArgumentParser("telegramctl", add_help=False)
group = parser.add_argument_group("admin")
group.add_argument("--promote", nargs="+", help="提权", metavar=("用户", "权限"))
group.add_argument("--demote", nargs="+", help="降权", metavar=("用户", "权限"))
parser.add_argument(
    "--mute", nargs="+", help="静言", metavar=("[持续时间] 用户", "用户")
)
parser.add_argument("--unmute", nargs="+", help="解除静言", metavar="用户")
parser.add_argument("--kick", nargs="+", help="踢出", metavar="用户")
parser.add_argument(
    "--ban", nargs="+", help="封禁", metavar=("[持续时间] 用户", "用户")
)
parser.add_argument("--unban", nargs="+", help="解除封禁", metavar="用户")
if __name__ == "__main__":
    parser.print_help()
    print(parser.parse_args())
