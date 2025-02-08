import os

from ruamel.yaml import YAML

config_path = "config.yaml"
if not os.path.exists(config_path):
    if os.name == "nt":
        base_dir = os.getenv("APPDATA", os.path.expanduser(r"~\AppData\Roaming"))
    else:
        base_dir = os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    config_path = os.path.join(base_dir, "tgbot", "config.yaml")

CONFIG: dict = dict()
with open(config_path) as file:
    CONFIG = YAML().load(file)
