from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from text import order_text


shop_router = Router()
@shop_router.message(Command('shop'))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Обувь'),
                KeyboardButton(text='Футболки'),
                KeyboardButton(text='Брюки'),
                KeyboardButton(text='Куртки')
            ],
            [
                KeyboardButton(text='Оформить заказ')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите раздел ↓ ', reply_markup=kb)

@shop_router.message(F.text == 'Обувь')
async def shoes(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекции обуви в нашем магазине:', 'images/shoes.jpg',
    reply_markup=kb)

@shop_router.message(F.text == 'Футболки')
async def t_shirts(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция футболок в нашем магазине:', 'images/t_shirts.jpg',
    reply_markup=kb)

@shop_router.message(F.text == 'Брюки')
async def trousers(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция брюк в нашем магазине:', 'images/trousers.jpg',
    reply_markup=kb)

@shop_router.message(F.text == 'Куртки')
async def jackets(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция курток в нашем магазине:', 'images/jackets.jpg',
    reply_markup=kb)

@shop_router.message(F.text == 'Оформить заказ')
async def order(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer(order_text, reply_markup=kb)
