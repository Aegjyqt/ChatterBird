from aiogram import Bot, Dispatcher, types, executor

import input, messages
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def greetings(message: types.Message):
    await message.answer(messages.welcome)


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.answer(messages.about)


@dp.message_handler()
async def commence(message: types.Message):
    string = message.text
    temp = input.Input(string)
    output = temp.translate()
    if output == 'Простите, я только учусь! Но на всякий случай, попробуем ввести в именительном падеже?':
        await message.answer('Не знаю!')
    else:
        await message.answer('Знаю!')
    await message.answer(output)
    await message.answer('(данных по актуальности нет без доступа к данным Переводчика. Увы!)')


executor.start_polling(dp)
