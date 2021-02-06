import os

def package_path(*paths, package_directory=os.path.dirname(os.path.abspath(__file__))):
  return os.path.join(package_directory, *paths)

m_start = "Тут Ви можете отримати інформацію про:\n\
  - контакти підрозділів Експертної служби МВС України \U0001F1FA\U0001F1E6\n\
(розклад роботи, телефон, факс, адресу та електронні адреси)\n\
  - ціни на послуги"
m_hi = "Вас вітає ex-bot! \U0001F44B\n"+m_start
m_dep = "Оберіть підрозділ, про який Ви хочите отримати інформацію:"
m_Info = "Оберіть про що Ви хотілиб дізнатися"

MESSAGES = {
  'start': m_start,
  'deps': m_dep,
  'hi': m_hi,
  'info': m_Info,
}

def getDepInfoByType(id, type='contacts'):
  return open(package_path(f'dep{id}',f'{type}.md'),'r').read()