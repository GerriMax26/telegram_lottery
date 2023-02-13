from aiogram import Bot,Dispatcher,executor,types
import markups as nav
from translation import translation_text
from db import Database
from questions import registrations
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from FSM import UserState
from aiogram.dispatcher import FSMContext

#C:/Users/GaraevMaksim/Desktop/token.txt

with open('C:/Users/GaraevMaksim/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

storage = MemoryStorage()

dp = Dispatcher(bot,storage=storage)

db = Database()

array_response = []


@dp.message_handler(commands=['start']) 
async def start_command(message: types.Message):
    
    if not db.user_exists(message.from_user.id):
        
        await bot.send_message(message.from_user.id, 
                               'Choise language:',
                         reply_markup=nav.lang_menu)
    else:
        lang = db.get_lang(message.from_user.id)
            
        await bot.send_message(message.from_user.id, 
                            translation_text('Привет!',lang),
                            reply_markup=nav.main_menu(lang))


@dp.callback_query_handler(text_contains = 'lang_')
async def set_language(callback: types.CallbackQuery):
    
    await bot.delete_message(callback.from_user.id,
                             callback.message.message_id)
    
    if not db.user_exists(callback.from_user.id):
        
        lang = callback.data[5:]
        
        db.add_user(callback.from_user.id,
                    lang)
        
    await bot.send_message(callback.from_user.id, 
                           translation_text('Привет!',lang),
                           reply_markup=nav.main_menu(lang))


@dp.message_handler(text = ['Регистрация','Registration','Registro'])
async def user_register(message: types.Message):
    await UserState.full_name.set()
    
    lang = db.get_lang(message.from_user.id)
    
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(0),lang))

@dp.message_handler(state = UserState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(full_name=message.text)
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(1),lang))
    await UserState.next()

@dp.message_handler(state = UserState.country)
async def get_country(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(country=message.text)
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(2),lang))
    await UserState.next()
    
@dp.message_handler(state = UserState.city)
async def get_city(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(city=message.text)
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(3),lang))
    await UserState.next()

@dp.message_handler(state = UserState.address)
async def get_address(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(address=message.text)
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(4),lang))
    await UserState.next()

@dp.message_handler(state = UserState.postcode)
async def get_postcode(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(postcode=message.text)
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(5),lang))
    await UserState.next()

@dp.message_handler(state = UserState.phone)
async def get_phone(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(phone=message.text)
    await bot.send_message(message.from_user.id,
                               translation_text(registrations(6),lang))
    await UserState.next()

@dp.message_handler(state = UserState.email)
async def get_email(message: types.Message, state: FSMContext):
    global array_response
    lang = db.get_lang(message.from_user.id)
    await state.update_data(email=message.text)
    data = await state.get_data()
    for i in data:
        array_response.append(data[i])
    db.add_info_user(array_response,
                        message.from_user.id,
                        lang)
    await bot.send_message(message.from_user.id,
                               translation_text('Успешная регистрация!',lang))              
    await state.reset_state(with_data=False)
    

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)