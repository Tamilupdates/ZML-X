import logging
from requests import get as rget
import os

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL')
try:
    if not CONFIG_FILE_URL:
        raise ValueError("CONFIG_FILE_URL is missing or empty")

    res = rget(CONFIG_FILE_URL)
    if res.status_code == 200:
        with open('config.env', 'wb+') as f:
            f.write(res.content)
    else:
        LOGGER.error(f"Failed to download config.env {res.status_code}")
except Exception as e:
    LOGGER.error(f"Error downloading CONFIG_FILE_URL: {e}")