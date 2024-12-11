from ..constants import HF_ASSETS_CACHE as HF_ASSETS_CACHE
from pathlib import Path

def cached_assets_path(library_name: str, namespace: str = 'default', subfolder: str = 'default', *, assets_dir: str | Path | None = None): ...
