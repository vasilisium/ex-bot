from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State
from aiogram.utils import executor
from . import config

from .messages.all import MESSAGES as msg
from .messages.all import getDepInfoByType

from .keyboards.start import startKeyboard, devKeyboard

from .keyboards.deps import kbList
from .keyboards.deps import kbMenu
from .keyboards.deps import kbInfo

import aiohttp
import asyncio

"""Отримання твмісту *.md файлів з githab для певного підрозділу за типом інформації відображення
id - ідентифікатор підрозділу
type - тип інформації, а фактично ім'я файлу (за замовченням 'contacts')
"""
async def getMsg(id, type='contacts'):
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://raw.githubusercontent.com/vasilisium/ex-bot/main/messages/dep{id}/{type}.md') as response:
      status = response.status
      if status == 200:
        m = await response.text()
        return m
      
      return msg['dev']

bot = Bot(token=config.BOT_API_KEY)
dp = Dispatcher(bot, storage=config.MemoryStorage())
dp.middleware.setup(config.LoggingMiddleware())

@dp.message_handler(Command("start"))
async def start_command_handler(message:types.Message):
  await message.answer(msg['hi'], reply_markup=startKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'home')
async def show_start_messame(callback_query: types.CallbackQuery, state: config.FSMContext):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(msg['start'])
  await callback_query.message.edit_reply_markup(startKeyboard)
  await state.reset_state()

@dp.callback_query_handler(lambda c: c.data == 'getDeps')
async def show_deps(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(msg['deps'])
  await callback_query.message.edit_reply_markup(kbList)

@dp.callback_query_handler(lambda c: c.data.startswith('depInfo'))
async def show_dep_menu(callback_query: types.CallbackQuery, state:config.FSMContext):
  await bot.answer_callback_query(callback_query.id)
  
  dep_id = int(callback_query.data[7:])
  # await ExStates.sDep.set()
  async with state.proxy() as data:
    data['dep_id'] = dep_id

  depMsg = await getMsg(dep_id)

  await callback_query.message.edit_text(depMsg, parse_mode='Markdown')
  await callback_query.message.edit_reply_markup(kbMenu)

@dp.callback_query_handler(lambda c: c.data == 'depsInfo')
async def show_dep_menu(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  
  await callback_query.message.edit_text(msg['info'])
  await callback_query.message.edit_reply_markup(kbInfo)

@dp.callback_query_handler(lambda c: c.data in ['contacts', 'administration', 'hours', 'aditional'])
async def show_info_of_type(callback_query: types.CallbackQuery, state: config.FSMContext):
  await bot.answer_callback_query(callback_query.id)
  
  data = await state.get_data()
  dep_id = data.get('dep_id')
  if dep_id is not None :
    depMsg = await getMsg(dep_id, callback_query.data)

    await callback_query.message.edit_text(depMsg, parse_mode='Markdown')
    await callback_query.message.edit_reply_markup(kbMenu)
  else:
    await callback_query.message.edit_text(msg['deps'])
    await callback_query.message.edit_reply_markup(kbList)

@dp.callback_query_handler(lambda c: c.data == 'btnPrices')
async def show_services(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id)
  await callback_query.message.edit_text(msg['uc'])
  await callback_query.message.edit_reply_markup(devKeyboard)

async def shutdown(dispatcher: Dispatcher):
  await dispatcher.storage.close()
  await dispatcher.storage.wait_closed()

def start():
  print("executor -> start_polling")
  executor.start_polling(dp, on_shutdown=shutdown)

if __name__ == '__main__':
  start()