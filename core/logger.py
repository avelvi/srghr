import logging
from core.config import Config

config = Config()
config.parse()

level = config.get('log.level')

logging.basicConfig(level=level)
logger = logging
