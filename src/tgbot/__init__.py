import os

from ruamel.yaml import YAML

config_path = "config.yaml"
if not os.path.exists(config_path):
    xdg_config_home = os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    config_path = os.path.join(xdg_config_home, "tgbot", "config.yaml")

CONFIG: dict = dict()
with open(config_path) as file:
    CONFIG = YAML().load(file)
