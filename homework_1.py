import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram.filters import Command


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Добавить боту 3 обработчика
# 1) Команда 'start' должна приветствовать по имени
@dp.message(Command('start'))
async def start(message: types.Message):
    print(message.from_user)
    await message.answer(f'Здравствуйте {message.from_user.first_name}')

# 2) Команда 'myinfo' должна отправлять его данные(id, first_name, username)
@dp.message(Command('myinfo'))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}')
    await message.answer(f'Ваше имя: {message.from_user.first_name}')
    await message.answer(f'Ваше имя пользователя: {message.from_user.username}')

# 3) Команда 'picture' должна олправлять пользователю случайную картинку из папки images
@dp.message(Command('picture'))
async def send_photo(message: types.Message):
    file = types.FSInputFile('images/bb.gif')
    await message.answer_animation(file)

async def homework_1():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(homework_1())