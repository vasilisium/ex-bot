from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# Dispatcher, executor,

if __name__ != '__main__':
  from . import config
else:
  import config

bot = Bot(token=config.BOT_API_KEY)
dp = Dispatcher(bot, storage=config.MemoryStorage())
dp.middleware.setup(config.LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start_command_handler(message:types.Message):
  await message.reply()

@dp.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)

async def shutdown(dispatcher: Dispatcher):
  await dispatcher.storage.close()
  await dispatcher.storage.wait_closed()

def start():
  print("executor -> start_polling")
  executor.start_polling(dp, on_shutdown=shutdown)

if __name__ == '__main__':
  start()