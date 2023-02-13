import logging

from aiogram import *

API_TOKEN = '6182223388:AAFwKK-bc09aNNl0dwv3w49NNrHTJJsH7Cs'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("hello\n i find your age")


@dp.message_handler(commands=['age'])
async def age(message: types.Message):
    await message.answer("Enter birth year:")


@dp.message_handler()
async def age_calc(message: types.Message):
    result = 2023 - int(message.text)
    await message.answer(f"Your age: {result}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)