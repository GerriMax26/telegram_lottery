from aiogram import Bot,Dispatcher,executor,types
import markups as nav
from translation import translation_text
from db import Database

with open('C:/Users/GaraevMaksim/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

db = Database()


@dp.message_handler(commands=['start']) 
async def start_command(message: types.Message):
    
    if not db.user_exists(message.from_user.id):
        
        await bot.send_message(message.from_user.id, 
                               'Choise language:',
                         reply_markup=nav.lang_menu)



@dp.callback_query_handler(text_contains = 'lang_')
async def set_language(callback: types.CallbackQuery):
    
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    
    if not db.user_exists(callback.from_user.id):
        
        lang = callback.data[5:]
        
        db.add_user(callback.from_user.id,
                    lang)
        
    await bot.send_message(callback.from_user.id, 
                           translation_text('Привет!',lang),
                           reply_markup=nav.main_menu(lang))


@dp.message_handler()
async def mess(message: types.Message):
    
    await bot.send_message(message)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)