import logging
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

BOT_API_KEY=os.getenv('BOT_KEY')

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s' \
  , level=logging.DEBUG, filename='log.txt')