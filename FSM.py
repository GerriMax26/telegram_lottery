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

    
