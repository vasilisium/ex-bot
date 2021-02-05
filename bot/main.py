from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# if __name__ != '__main__':
from . import config

from .messages.all import MESSAGES as msg
from .messages.all import getDepInfo

from .keyboards.start import startKeyboard

from .keyboards.deps import kbList
from .keyboards.deps import kbMenu
from .keyboards.deps import kbInfo

# else:
#   import config

bot = Bot(token=config.BOT_API_KEY)
dp = Dispatcher(bot, storage=config.MemoryStorage())
dp.middleware.setup(config.LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start_command_handler(message:types.Message):
  await message.answer(msg['hi'], reply_markup=startKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'home')
async def show_start_messame(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(msg['start'])
  await callback_query.message.edit_reply_markup(startKeyboard)

@dp.callback_query_handler(lambda c: c.data =='getDeps')
async def show_deps(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(msg['deps'])
  await callback_query.message.edit_reply_markup(kbList)

@dp.callback_query_handler(lambda c: c.data.startswith('depInfo'))
async def show_dep_menu(callback_query: types.CallbackQuery):
  dep_id = int(callback_query.data[7:])

  await callback_query.message.edit_text(getDepInfo(dep_id), parse_mode='Markdown')
  # print(await callback_query.message.conf)
  await callback_query.message.edit_reply_markup(kbMenu)

@dp.callback_query_handler(lambda c: c.data == 'depsInfo')
async def show_dep_menu(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(msg['info'])
  await callback_query.message.edit_reply_markup(kbInfo)

@dp.callback_query_handler(lambda c: c.data in ['contacts', 'administration', 'hours', 'aditional'])
async def show_info_of_type(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(getDepInfo(last_dep_id, callback_query.data), parse_mode='Markdown')
  await callback_query.message.edit_reply_markup(kbMenu)

async def shutdown(dispatcher: Dispatcher):
  await dispatcher.storage.close()
  await dispatcher.storage.wait_closed()

def start():
  print("executor -> start_polling")
  executor.start_polling(dp, on_shutdown=shutdown)

if __name__ == '__main__':
  start()