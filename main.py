import os
from datetime import datetime
import time
from datetime import date

from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from aiogram.dispatcher.filters import Text
import schedule

from translation import translation_text
from db import Database
from questions import registrations
from questions import withdraw_money
from FSM import UserState
from FSM import BuyState
from FSM import WithdrawMoney
from FSM import JackpotState
from generation_number_win_ticket import generation_win_ticket
from calculation_winnings import calculation_win
from calculation_referal_program import calculation_referal
import markups as nav


WIN_TICKET = 0

load_dotenv()

TOKEN_API = os.getenv('TOKEN')

bot = Bot(TOKEN_API)

storage = MemoryStorage()

dp = Dispatcher(bot,storage=storage)

db = Database()

array_response = []


'''Добавил кнопку'''    
@dp.message_handler(commands=['start']) 
async def start_command(message: types.Message):
    #проверка, что в бд такого уже нет

    
    if not db.user_exists(message.from_user.id):
        db.add_referal_link(message.from_user.id)
        args = message.get_args()
    
        if args: 
            id_referal = args[1]
            db.add_id_referal(id_referal)
        
        else:
            db.add_id_referal(0,message.from_user.id)
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
        
    lang = callback.data[5:]
        
    db.add_user(callback.from_user.id,
                    lang)
        
    await bot.send_message(callback.from_user.id, 
                           translation_text('Привет!',lang),
                           reply_markup=nav.main_menu(lang))

#Начало анкетирования для регистрации

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
                        message.from_user.id 
                        )
    await bot.send_message(message.from_user.id,f"{data['full_name']},"+
                               translation_text('Регистрация завершена!',lang),
                               reply_markup=nav.next_menu(lang,message.from_user.id))
    
    await bot.send_message(os.getenv('id_admin'),db.get_all_data_user(message.from_user.id))
        
    await state.finish()

#Конец анкетирования для регистрации

@dp.message_handler(text = ['Лотерея','Lottery','Lotería'])
async def button_buy_ticket(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    await bot.send_message(message.from_user.id,
                               translation_text('Купить билет',lang),#Поменять сообщение Купить билет
                               reply_markup=nav.buy_ticket(lang))

@dp.callback_query_handler(Text(startswith = 'buy')) 
async def buy_ticket(callback: types.CallbackQuery):
    
    lang = db.get_lang(callback.from_user.id)
    
    payment = True # так как нет реализации оплаты, payment всегда True
    
    #блок с оплатой
    
    if (payment):
        
        await bot.send_message(callback.from_user.id, 
                           translation_text('Оплата прошла успешно!',lang))

        await bot.send_message(os.getenv('id_admin'), 
                           f'{db.get_all_data_user(callback.from_user.id)} купил билет.') 
        
        db.add_payment(payment,callback.from_user.id) #Фиксируем факт оплаты 
        
        if(db.check_id_referal(callback.from_user.id) != 0): 
            
            db.update_balance_user(db.check_id_referal(callback.from_user.id),
                                   calculation_referal(lang))
            
        await BuyState.send_number.set()
        
        await bot.send_message(callback.from_user.id, 
                           translation_text('Отправьте число из 8-и цифр',lang))


@dp.message_handler(state = BuyState.send_number) 
async def get_send_numbers(message: types.Message, state: FSMContext):
    
       
    lang = db.get_lang(message.from_user.id)
       
    await state.update_data(send_number=message.text)
       
    data = await state.get_data() #получаем введенный номер пользователя
       
    db.add_user_ticket(message.from_user.id,data['send_number']) #Добавить в БД номер билета, который ввел пользователь
       
    id_win_ticket = generation_win_ticket(message.from_user.id) #Генерация выигрышного билета
       
    await bot.send_message(message.from_user.id,
                               translation_text('Номер выигрышного билета: '+ f"{id_win_ticket}",
                                                lang)) #до сюда ок

    result_win = calculation_win(data['send_number'],id_win_ticket,lang) #Расчет выигрыша
    
    db.add_prize(result_win,message.from_user.id) #добавляем в БД размер выигрыша
    
    db.update_balance_user(message.from_user.id,result_win)#Обновляем баланс у пользователя
    
    await state.reset_state(with_data=False)
    
    await bot.send_message(message.from_user.id,
                               translation_text('Ваш выигрыш: '+ f"{result_win}" + translation_text('рублей',lang),
                                                lang),
                               reply_markup=nav.buy_ticket(lang))
    
    await bot.send_message(os.getenv('id_admin'),db.get_all_data_user(message.from_user.id) + 'выиграл' + translation_text(f"{result_win}" + translation_text('рублей',lang),
                                                lang))
    
@dp.callback_query_handler(Text(startswith= 'back'))
async def back_menu(callback: types.CallbackQuery):
    lang = db.get_lang(callback.from_user.id)
    await bot.send_message(callback.from_user.id,
                               translation_text('Главное меню',lang),
                               reply_markup=nav.next_menu(lang,callback.from_user.id))


@dp.message_handler(text = ['Инструкция','Instruction','Instrucciones']) #Поправить ссылки, но не критично
async def get_instruction(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    if lang == 'ru':
        with open('C:/Users/admin/Desktop/telegram_lottery/instruction/instruction_ru.txt','r') as file:
            
            await bot.send_message(message.from_user.id,
                               file.read())
    elif(lang == 'en'):
        
        with open('C:/Users/admin/Desktop/telegram_lottery/instruction/instruction_en.txt','r') as file:
            
            await bot.send_message(message.from_user.id,
                               file.read())
    else:
        with open('C:/Users/admin/Desktop/telegram_lottery/instruction/instruction_es.txt','r') as file:
            
            await bot.send_message(message.from_user.id,
                                   file.read())
    

@dp.message_handler(text = ['Поддержка','Soporte','Support'])      
async def get_support(message: types.Message):
    
    lang = db.get_lang(message.from_user.id)
    await bot.send_message(message.from_user.id,
                           translation_text('Какой-то текст'+'https://t.me/moxxx2',lang)    
    )


@dp.message_handler(text = ['Personal account','Личный кабинет','Área personal'])
async def get_info_personal_account(message: types.Message):
    
    lang = db.get_lang(message.from_user.id)
    
    await bot.send_message(message.from_user.id,
                           translation_text('Ваш баланс:',lang) + str(db.get_balance_user(message.from_user.id)) + translation_text('рублей',lang) 
                           + translation_text('Размер джекпота: ',lang)+ str(db.get_jackpot_prize()) + translation_text('рублей',lang),
                           reply_markup=nav.withdraw_money(lang)    
    )


@dp.callback_query_handler(Text(startswith = 'money'))
async def withdraw_money(callback:types.CallbackQuery):
    
    await WithdrawMoney.summ.set()
    
    lang = db.get_lang(callback.from_user.id)
    
    await bot.send_message(callback.from_user.id,
                               translation_text(withdraw_money(0),lang))
    

@dp.message_handler(state = WithdrawMoney.summ)
async def get_summ(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    
    await state.update_data(summ=message.text)
    
    data = await state.get_data()
    
    if(db.get_balance_user(message.from_user.id) >= data[0]):
        
        await bot.send_message(message.from_user.id,
                                translation_text(withdraw_money(1),lang))
        await WithdrawMoney.next()
    else:
        await state.reset_state(with_data=False)
        await bot.send_message(message.from_user.id,
                                translation_text('Недостаточно средств на балансе, уĸажите другую сумму!',lang))
        
        await WithdrawMoney.summ.set()
    

@dp.message_handler(state = WithdrawMoney.card_number)
async def get_card_number(message:types.Message, state:FSMContext):
    
    lang = db.get_lang(message.from_user.id)
    
    await state.update_data(card_number=message.text)
    
    await bot.send_message(message.from_user.id,
                               translation_text('Заявĸа принята, ожидайте ответ от поддержĸи.',lang))
    
    data = await state.get_data()
    
    await bot.send_message(os.getenv('id_admin'),db.get_all_data_user(message.from_user.id) + f'сумма для вывода: {data[0]}' + f'номер карты: {data[1]}')
    await state.reset_state(with_data=False)

@dp.message_handler(text = ['Реферальная программа','Referral program','Programa de referencia'])
async def get_referal_link(message:types.Message):
    
    lang = db.get_lang(message.from_user.id)
    
    await bot.send_message(message.from_user.id,
                               translation_text('Какой-то текст',lang)+db.get_referal_link(message.from_user.id))
    
@dp.message_handler(text=['Джекпот','Jackpot'])
async def get_jackpot(message:types.Message):
    
    lang = db.get_lang(message.from_user.id)
    
    today = date.today()
    if(today[5:len(today)] != '12-31'):
        
        array_date_jackpot = db.get_date_jackpot()
    
        for i in array_date_jackpot: #получаем id_jackpot использую текущую дату
            for j in i:
                if (datetime.now() >= j[1] and datetime.now() <= j[2]):
                    id_jackpot = j[0]
                    break
        if(message.from_user.id not in db.get_all_jackpot_user(id_jackpot)):
            await bot.send_message(message.from_user.id,
                            translation_text(f'Размер джекпота: ',lang)+str(db.get_jackpot_prize()),
                            reply_markup=nav.wanna_jackpot(lang))
        else:
            await bot.send_message(message.from_user.id,
                        translation_text('Вы уже зарегистрированы в лотерее!',lang))
    else:
        await bot.send_message(message.from_user.id,
                        translation_text('Регистрация билетов для участия в Джекпоте завершена!',lang))
    
@dp.callback_query_handler(Text(startswith= 'jackpot'))
async def jackpot(callback:types.CallbackQuery):
    
    lang = db.get_lang(callback.from_user.id)
    
    await JackpotState.send_number.set()
        
    await bot.send_message(callback.from_user.id, 
                           translation_text('Отправьте число из 8-и цифр',lang))

@dp.message_handler(state = JackpotState.send_number)
async def get_send_number(message: types.Message, state: FSMContext):
    
    lang = db.get_lang(message.from_user.id)
       
    await state.update_data(send_number=message.text)
    
    data = await state.get_data()
    
    array_date_jackpot = db.get_date_jackpot()
    
    for i in array_date_jackpot: #получаем id_jackpot использую текущую дату
        for j in i:
            if (datetime.now() >= j[1] and datetime.now() <= j[2]):
                id_jackpot = j[0]
                break
        
    db.add_jackpot_ticket(id_jackpot,message.from_user.id,data[0])
    
    await bot.send_message(message.from_user.id, 
                           translation_text('Ваш билет зарегистрирован!',lang))
    

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
    
    schedule.every().day.at('00:00').do(generation_win_ticket)
    while True:
        schedule.run_pending()
        time.sleep(86400)
    
    