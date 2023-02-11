from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import markups as nav
from translation import translation_text
with open('C:/Users/GaraevMaksim/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)




@dp.message_handler(commands=['start']) 
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choise language:',
                         reply_markup=nav.lang_menu)
    await bot.send_message(message.from_user.id,'Выбор',reply_markup=nav.main_menu('en'))
    await message.delete()


@dp.callback_query_handler(text_contains = 'lang_')
async def set_language(callback: types.CallbackQuery):
    #await bot.delete_message(callback.from_user.id, callback.message.message_id)
    lang = callback.data[5:]
    await bot.send_message(callback.from_user.id, 
                           translation_text('Привет!',lang))

@dp.message_handler()
async def mess(message: types.Message):
    await bot.send_message(message)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)