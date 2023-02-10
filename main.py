from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

with open('C:/Users/admin/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True) #аргументы

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')

kb.insert(b1).insert(b2).insert(b3)

HELP_COMMAND = '''
<b>/help</b> - <em>Список команд</em>
<b>/start</b> - <em>Старт бота</em>
<b>/description</b> - <em>Описание бота</em>
<b>/photo</b> - <em>Отправка фото</em>
'''

@dp.message_handler(commands=['help']) #декоратор обработки
async def help_command (message: types.Message):
    await message.answer(text = HELP_COMMAND, 
                           parse_mode = 'HTML') #Перевод текста в верхний регистр
    await message.delete()

@dp.message_handler(commands=['start']) #декоратор обработки
async def start_command(message: types.Message):
    await message.answer(text = 'Hello World!',
                         reply_markup=kb) #Перевод текста в верхний регистр
    await message.delete()

@dp.message_handler(commands=['description']) #декоратор обработки
async def description_command (message: types.Message):
    await message.answer(text = 'Наш бот умеет то  и то')
    await message.delete()

@dp.message_handler(commands=['photo']) #декоратор обработки
async def photo_command (message: types.Message):
    await bot.send_photo(message.chat.id,photo = 'https://chudo-prirody.com/uploads/posts/2021-08/1628905018_79-p-skachat-foto-milikh-kotikov-85.jpg')
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
    