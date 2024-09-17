import shutil
import logging
import requests

from tqdm import tqdm

from .path_util import get_cache_dir, get_model_data_dir, get_model_data_dir_name_versioned

DEFAULT_DOWNLOAD_URL = f"https://biocentral.cloud/downloads/bio_ml_models/{get_model_data_dir_name_versioned()}.zip"

logger = logging.getLogger(__name__)


def ensure_downloaded(custom_download_url=None):
    if custom_download_url is None:
        custom_download_url = DEFAULT_DOWNLOAD_URL
    model_data_dir = get_model_data_dir()
    if model_data_dir.exists():
        logger.info(f"Model data already downloaded, location: {model_data_dir}")
    else:
        _download_model_data(custom_download_url)
        logger.info(f"Model data downloaded, location: {model_data_dir}")


def _download_model_data(url):
    cache_dir = get_cache_dir()
    model_data_file = cache_dir / get_model_data_dir_name_versioned()
    zip_file = model_data_file.with_suffix('.zip')

    try:
        logger.info(f"Downloading model data from {url}..")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192  # 8 KB

        with open(zip_file, "wb") as f, tqdm(
                desc="Downloading model data",
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as progress_bar:
            for data in response.iter_content(block_size):
                size = f.write(data)
                progress_bar.update(size)

        logger.info("Unpacking model data archive..")
        shutil.unpack_archive(zip_file, model_data_file)

        # Remove the zip file after successful extraction
        zip_file.unlink()

        logger.info("Model data downloaded and unpacked successfully!")

    except requests.RequestException as e:
        logger.error(f"Error downloading model data: {e}")
        if zip_file.exists():
            zip_file.unlink()
        raise

    except shutil.ReadError as e:
        logger.error(f"Error unpacking model data: {e}")
        if zip_file.exists():
            zip_file.unlink()
        raise

    except Exception as e:
        logger.error(f"Unexpected error while retrieving model data: {e}")
        if zip_file.exists():
            zip_file.unlink()
        raise
