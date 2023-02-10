from aiogram import Bot,Dispatcher,executor,types

with open('C:/Users/admin/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

@dp.message_handler() #декоратор обработки
async def echo_upper (message: types.Message):
    await message.answer(text = message.text.upper()) #Перевод текста в верхний регистр



if __name__ == '__main__':
    executor.start_polling(dp)
    