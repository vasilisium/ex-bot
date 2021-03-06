# import os
import importlib

# def package_path(*paths, package_directory=os.path.dirname(os.path.abspath(__file__))):
#   return os.path.join(package_directory, *paths)

m_start = "Тут Ви можете отримати інформацію про:\n\
  - контакти підрозділів Експертної служби МВС України \U0001F1FA\U0001F1E6\n\
(розклад роботи, телефон, факс, адресу та електронні адреси)\n\
  - перелік послуг та реквізити для оплати цих послуг"
m_hi = "Вас вітає ex-bot! \U0001F44B\n"+m_start
m_dep = "Оберіть підрозділ, про який Ви хочите отримати інформацію:"
m_Info = "Оберіть про що Ви хотілиб дізнатися"
m_dev = """\
Інформаця відсутня через те, що розробник не бачить сенсу *в ручному режимі* переносити всю інформацію у бот.\n
Пропонується створення API, з якого централізовано братиметься інформація для бота та інших потреб (сайтів)...\n
_Наразі доступна інформація тільки по ДНД (перший підрозділ)_
Пишіть мені: @Vasilisium"""
m_underConstruction = "В розробці... \U0001F477"

MESSAGES = {
  'start': m_start,
  'deps': m_dep,
  'hi': m_hi,
  'info': m_Info,
  'dev': m_dev,
  'uc': m_underConstruction,
}

def getDepInfoByType(id, type='contacts'):
  spec = importlib.util.find_spec(f'.{type}', package=f'.messages.dep{id}')
  m = spec.loader.load_module()
  # m = importlib.import_module(f'{type}', package=f'.messages.dep{id}')
  msg = m.msg
  # from .dep0 import contacts
  # msg = contacts.msg
  return msg