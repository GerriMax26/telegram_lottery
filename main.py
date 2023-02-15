from aiogram import Bot,Dispatcher,executor,types
import markups as nav
from translation import translation_text
from db import Database
from questions import registrations
from questions import withdraw_money
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from FSM import UserState
from FSM import BuyState
from FSM import WithdrawMoney
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

array_response = []#проверить используется ли


@dp.message_handler(commands=['start']) 
async def start_command(message: types.Message):
    db.add_referal_link(message.from_user.id)
    args = message.get_args()
    
    if args: #Проверить, если человек уже был в БД, реферальную ссылку не меняем
        id_referal = args[1]
        db.add_id_referal(id_referal)
        
    else:
        db.add_id_referal(0)
    
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

@dp.callback_query_handler(text_containce = 'buy') #Проверка, если есть реферал, ему отчислить 5%
async def buy_ticket(callback: types.CallbackQuery):
    
    lang = db.get_lang(callback.from_user.id)
    
    payment = True # так как нет реализации оплаты, payment всегда True
    
    #блок с оплатой
    
    if (payment):
        
        await bot.send_message(callback.from_user.id, 
                           translation_text('Оплата прошла успешно!',lang))

        db.add_payment(payment) #Фиксируем факт оплаты
        
        await BuyState.send_number.set()
        
        await bot.send_message(callback.from_user.id, 
                           translation_text('Отправьте число из 8-и цифр',lang))


@dp.message_handler(state = BuyState.send_number)
async def get_send_numbers(message: types.Message, state: FSMContext):
    
       
    lang = db.get_lang(message.from_user.id)
       
    await state.update_data(send_number=message.text)
       
    data = await state.get_data() #получаем введенный номер пользователя
       
    db.add_user_ticket(message.from_user.id,data[0]) #Добавить в БД номер билета, который ввел пользователь
       
    id_win_ticket = generation_win_ticket(message.from_user.id) #Генерация выигрышного билета
       
    await bot.send_message(message.from_user.id,
                               translation_text('Номер выигрышного билета: '+ f"{id_win_ticket}",
                                                lang))
       
    result_win = calculation_win(data[0],id_win_ticket,lang) #Расчет выигрыша
    
    db.add_prize(result_win,message.from_user.id) #добавляем в БД размер выигрыша
    
    db.update_balance_user(message.from_user.id,result_win)#Обновляем баланс у пользователя
    
    await state.reset_state(with_data=False)
    
    await bot.send_message(message.from_user.id,
                               translation_text('Ваш выигрыш:'+ f"{result_win}" + translation_text('рублей',lang),
                                                lang),
                               reply_markup=nav.buy_ticket(lang))
    
    
@dp.callback_query_handler(text_containce = 'back')
async def back_menu(callback: types.CallbackQuery):
    lang = db.get_lang(callback.from_user.id)
    await bot.send_message(callback.from_user.id,
                               translation_text('Главное меню',lang),
                               reply_markup=nav.next_menu(lang))


@dp.message_handler(text = ['Инструкция','Instruction','Instrucciones'])
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
                           translation_text(f'Ваш баланс: {db.get_balance_user(message.from_user.id)} рублей',lang) 
                           + translation_text(f'Размер джекпота: ',lang), #добавить получение размера джекпота из БД
                           reply_markup=nav.withdraw_money(lang)    
    )


@dp.callback_query_handler(text_containce = 'money')
async def withdraw_money(callback:types.CallbackQuery):
    
    await WithdrawMoney.summ.set()
    
    lang = db.get_lang(callback.from_user.id)
    
    await bot.send_message(callback.from_user.id,
                               translation_text(withdraw_money(0),lang))
    
    #Проверка, что хватает денег

@dp.message_handler(state = WithdrawMoney.summ)
async def get_summ(message: types.Message, state: FSMContext):
    
    lang = db.get_lang(message.from_user.id)
    
    await state.update_data(summ=message.text)
    
    await bot.send_message(message.from_user.id,
                               translation_text(withdraw_money(1),lang))
    await UserState.next()

@dp.message_handler(state = WithdrawMoney.card_number)
async def get_card_number(message:types.Message, state:FSMContext):
    
    lang = db.get_lang(message.from_user.id)
    
    await state.update_data(card_number=message.text)
    
    await bot.send_message(message.from_user.id,
                               translation_text('Заявĸа принята, ожидайте ответ от поддержĸи.',lang))
    
    #Отправить данные админу
    await state.reset_state(with_data=False)


    
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)