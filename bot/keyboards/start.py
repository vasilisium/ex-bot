from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn_departments = InlineKeyboardButton('\U0001F3E2 Обрати підрозділ', callback_data='getDeps')
btn_price = InlineKeyboardButton('\U0001F4B2 Ціни на послуги', callback_data='btnPrices')
startKeyboard = InlineKeyboardMarkup(row_width=2).add(btn_departments, btn_price)