from aiogram import Bot,Dispatcher,executor,types

with open('C:/Users/admin/Desktop/token.txt','r') as file:
    TOKEN_API = file.readline()

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

HELP_COMMAND = '''
/help - список команд
/start - начать работу с ботом
'''
@dp.message_handler(commands=['help']) #декоратор обработки
async def help_command (message: types.Message):
    await message.reply(text = HELP_COMMAND) #Перевод текста в верхний регистр

@dp.message_handler(commands=['start']) #декоратор обработки
async def start_command(message: types.Message):
    await message.answer(text = 'Hello World!') #Перевод текста в верхний регистр
    await message.delete()
    

if __name__ == '__main__':
    executor.start_polling(dp)
    