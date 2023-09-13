from aiogram import types, Router
from aiogram.filters import Command


info_router = Router()

@info_router.message(Command('myinfo'))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}')
    await message.answer(f'Ваше имя: {message.from_user.first_name}')
    await message.answer(f'Ваше имя пользователя: {message.from_user.username}')