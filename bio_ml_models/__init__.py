import sys
import logging
from typing import List, Dict

from bio_ml_models.proteins import ProteinTasks
from bio_ml_models.base import BioTaskCollection
from bio_ml_models.utils import ensure_downloaded


def _setup_logging():
    logger_format: str = "%(asctime)s %(levelname)s %(message)s"
    formatter = logging.Formatter(logger_format)

    # Create stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    stream_handler.setStream(sys.stdout)

    # Get the root logger and add handlers
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    # Capture warnings with the logging system
    logging.captureWarnings(True)


class BioModelCollection:
    def __init__(self, custom_download_url: str = None):
        _setup_logging()
        ensure_downloaded(custom_download_url=custom_download_url)
        self.proteins = ProteinTasks()

    def domain_dict(self) -> Dict[str, BioTaskCollection]:
        return {attr: getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), BioTaskCollection)}

    def domain_list(self) -> List[BioTaskCollection]:
        return list(self.domain_dict().values())

    def __getitem__(self, key):
        """
        This enables accessing the domains of the collection in a dict-like way.

        :param key: Domain name
        :return: Domain instance if the domain name is found
        """
        return getattr(self, key)


__all__ = ['BioModelCollection']
