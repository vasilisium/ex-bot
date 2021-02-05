from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

DEPS = {
  0: "\U0001F3AA Державний НДЕКЦ МВС України",
  1: "Вінницький",
  2: "Волинський",
  3: "Дніпропетровський",
  4: "Донецький",
  5: "Житомирський",
  6: "Закарпатський",
  7: "Запорізький",
  8: "Івано-Франківський",
  9: "Київський",
  10: "Кіровоградський",
  11: "Луганський",
  12: "Львівський",
  13: "Миколаївський",
  14: "Одеський",
  15: "Полтавський",
  16: "Рівненський",
  17: "Сумський",
  18: "Тернопільський",
  19: "Харківський",
  20: "\U0001F3AE Херсонський",
  21: "Хмельницький",
  22: "Черкаський",
  23: "Чернівецький",
  24: "Чернігівський",
}

kbList = InlineKeyboardMarkup()
kbList.row(InlineKeyboardButton(DEPS[0], callback_data="depInfo0"))

depsCount = DEPS.__len__()
for i in range(1, depsCount, 2):
  
  buttons_row = list()
  buttons_row.append(InlineKeyboardButton(DEPS[i], callback_data=f"depInfo{i}"))

  if i+1 <= depsCount-1:
    buttons_row.append(InlineKeyboardButton(DEPS[i+1], callback_data=f"depInfo{i+1}"))
  
  kbList.row(*tuple(buttons_row))
kbList.row(InlineKeyboardButton("До початку", callback_data="home"))

kbMenu = InlineKeyboardMarkup()
kbMenu.row( \
  InlineKeyboardButton("Інша інформація", callback_data="depsInfo"), \
  InlineKeyboardButton("Інний підрозділ", callback_data="getDeps"), \
  )
kbMenu.row(InlineKeyboardButton("До початку", callback_data="home"))

kbInfo = InlineKeyboardMarkup()
kbInfo.row(InlineKeyboardButton("Контакти", callback_data="contacts"))
kbInfo.row(InlineKeyboardButton("Керівництво", callback_data="administration"))
kbInfo.row(InlineKeyboardButton("Розклад роботи", callback_data="hours"))
kbInfo.row(InlineKeyboardButton("Додаткова інформація", callback_data="aditional"))
kbInfo.row(InlineKeyboardButton("До початку", callback_data="home"))