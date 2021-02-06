'''Module of states'''

from aiogram.dispatcher.filters.state import StatesGroup, State

'''States set
started state is state == None
'''
class ExStates(StatesGroup):
  '''state of chosen department'''
  sDep = State()

  '''state of prices (under cinstruction)'''
  sPrice = State()
  