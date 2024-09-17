import os

from pathlib import Path
from appdirs import user_cache_dir

from .version import __version__


def get_model_data_dir_name_versioned():
    return f"model_data_{__version__.replace('.', '-')}"


def get_model_data_dir():
    return get_cache_dir() / get_model_data_dir_name_versioned()


def get_cache_dir() -> Path:
    cache_dir = user_cache_dir("bio_ml_models")
    os.makedirs(cache_dir, exist_ok=True)
    return Path(cache_dir)
