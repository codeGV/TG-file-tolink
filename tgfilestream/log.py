
import logging

from .config import log_config, debug

if log_config:
    logging.basicConfig(filename=log_config)
else:
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    logging.getLogger("telethon").setLevel(logging.INFO if debug else logging.ERROR)

log = logging.getLogger("tgfilestream")
