from aiogram import Bot,Dispatcher,executor,types
import markups as nav
from translation import translation_text
from db import Database
from questions import registrations
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from FSM import UserState
from FSM import BuyState
from aiogram.dispatcher import FSMContext
from generation_number_win_ticket import generation_win_ticket
from calculation_winnings import calculation_win

#C:/Users/GaraevMaksim/Desktop/token.txt
#C:/Users/admin/Desktop/token.txt

with open('C:/Users/admin/Desktop/token.txt','r') as file:
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
    await bot.send_message(message.from_user.id,f"{data['full_name']},"+
                               translation_text('Регистрация завершена!',lang),
                               reply_markup=nav.next_menu(lang))
            
    await state.reset_state(with_data=False)


@dp.message_handler(text = ['Лотерея','Lottery','Lotería'])
async def button_buy_ticket(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    await bot.send_message(message.from_user.id,
                               translation_text('Купить билет',lang),
                               reply_markup=nav.buy_ticket(lang))

@dp.callback_query_handler(text_containce = 'buy')
async def buy_ticket(callback: types.CallbackQuery):
    
    lang = db.get_lang(callback.from_user.id)
    
    payment = True # так как нет реализации оплаты, payment всегда True
    
    #блок с оплатой
    if (payment):
        
        await bot.send_message(callback.from_user.id, 
                           translation_text('Оплата прошла успешно!',lang))

        db.add_payment(callback.from_user.id,
                       payment)
        
        await BuyState.send_number.set()
        
        await bot.send_message(callback.from_user.id, 
                           translation_text('Отправьте число из 8-и цифр',lang))

@dp.message_handler(state = BuyState.send_number)
async def get_send_numbers(message: types.Message, state: FSMContext):
    
       
    lang = db.get_lang(message.from_user.id)
       
    await state.update_data(send_number=message.text)
       
    data = await state.get_data()
       
    db.add_info_buy_tickets(message.from_user.id,data[0])
       
    id_win_ticket = generation_win_ticket(message.from_user.id,data[0])
       
    await bot.send_message(message.from_user.id,
                               translation_text('Номер выигрышного билета: '+ f"{id_win_ticket}",
                                                lang))
       
    result_win = calculation_win(data[0],id_win_ticket,lang)
    
    db.add_prize(result_win,message.from_user.id,data[0],id_win_ticket)
    
    await bot.send_message(message.from_user.id,
                               translation_text('Ваш выигрыш:'+ f"{result_win}" + translation_text('рублей',lang),
                                                lang),
                               reply_markup=nav.buy_ticket(lang))


        
                           
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)