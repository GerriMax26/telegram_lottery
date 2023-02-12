from aiogram import Bot,Dispatcher,executor,types
import markups as nav
from translation import translation_text
from db import Database
from questions import registrations

with open('C:/Users/GaraevMaksim/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

db = Database()

count = 0
array_response = []
flag = True
current_button = ''
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


@dp.message_handler()
async def mess(message: types.Message):
    
    global count
    
    global array_response
    
    global flag
    
    global current_button
    
    if(flag):
        current_button = message.text
        flag = False
    
    lang = db.get_lang(message.from_user.id)
    
    if current_button == translation_text('Регистрация',lang):
        
        array_response.append(message.text)
        
        await bot.delete_message(message.from_user.id,
                                 message.message_id)
        
        await bot.send_message(message.from_user.id,
                               translation_text(registrations(count),
                                                lang))
        
        if count <= 5:
             count += 1
        else:
            db.add_info_user(array_response,
                             message.from_user.id,
                             lang)
            count = 0
        
    
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)