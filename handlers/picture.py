from aiogram import types, Router, F
from aiogram.filters import Command


picture_router = Router()

@picture_router.message(Command('picture'))
async def send_photo(message: types.Message):
    files = types.FSInputFile('images/shop.gif')
    await message.answer_animation(files)

# @picture_router.message(F.text == 'Обувь')
# async def send_list(message: types.Message):
#     files = types.FSInputFile('images/shoes.jpg')
#     await message.answer_photo(files)
#
# @picture_router.message(F.text == 'Футболки')
# async def send_list(message: types.Message):
#     files = types.FSInputFile('images/t-shirts.jpg')
#     await message.answer_photo(files)
#
# @picture_router.message(F.text == 'Брюки')
# async def send_list(message: types.Message):
#     files = types.FSInputFile('images/trousers.jpg')
#     await message.answer_photo(files)
#
# @picture_router.message(F.text == 'Куртки')
# async def send_list(message: types.Message):
#     files = types.FSInputFile('images/jackets.jpg')
#     await message.answer_photo(files)

