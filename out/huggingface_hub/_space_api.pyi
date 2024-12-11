from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from huggingface_hub.utils import parse_datetime as parse_datetime

class SpaceStage(str, Enum):
    NO_APP_FILE = 'NO_APP_FILE'
    CONFIG_ERROR = 'CONFIG_ERROR'
    BUILDING = 'BUILDING'
    BUILD_ERROR = 'BUILD_ERROR'
    RUNNING = 'RUNNING'
    RUNNING_BUILDING = 'RUNNING_BUILDING'
    RUNTIME_ERROR = 'RUNTIME_ERROR'
    DELETING = 'DELETING'
    STOPPED = 'STOPPED'
    PAUSED = 'PAUSED'

class SpaceHardware(str, Enum):
    CPU_BASIC = 'cpu-basic'
    CPU_UPGRADE = 'cpu-upgrade'
    T4_SMALL = 't4-small'
    T4_MEDIUM = 't4-medium'
    L4X1 = 'l4x1'
    L4X4 = 'l4x4'
    ZERO_A10G = 'zero-a10g'
    A10G_SMALL = 'a10g-small'
    A10G_LARGE = 'a10g-large'
    A10G_LARGEX2 = 'a10g-largex2'
    A10G_LARGEX4 = 'a10g-largex4'
    A100_LARGE = 'a100-large'
    V5E_1X1 = 'v5e-1x1'
    V5E_2X2 = 'v5e-2x2'
    V5E_2X4 = 'v5e-2x4'

class SpaceStorage(str, Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

@dataclass
class SpaceRuntime:
    stage: SpaceStage
    hardware: SpaceHardware | None
    requested_hardware: SpaceHardware | None
    sleep_time: int | None
    storage: SpaceStorage | None
    raw: dict
    def __init__(self, data: dict) -> None: ...

@dataclass
class SpaceVariable:
    key: str
    value: str
    description: str | None
    updated_at: datetime | None
    def __init__(self, key: str, values: dict) -> None: ...
