from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    full_name = State()
    country = State()
    city = State()
    address = State()
    postcode = State()
    phone = State()
    email = State()

class BuyState(StatesGroup):
    send_number = State()
    
class WithdrawMoney(StatesGroup): #Поправить название
    summ = State()
    card_number = State()

class JackpotState(StatesGroup):
    send_number = State()
    