from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from text import order_text
from db.queries import get_product_by_category


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
    shoes1 = get_product_by_category(1)
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция обуви в нашем магазине:', reply_markup=kb)
    for s in shoes1:
        await message.answer(s[1])

@shop_router.message(F.text == 'Футболки')
async def t_shirts(message: types.Message):
    t_shirts1 = get_product_by_category(2)
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция футболок в нашем магазине:', reply_markup=kb)
    for t in t_shirts1:
        await message.answer(t[1])

@shop_router.message(F.text == 'Брюки')
async def trousers(message: types.Message):
    trousers1 = get_product_by_category(3)
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция брюк в нашем магазине:', reply_markup=kb)
    for t in trousers1:
        await message.answer(t[1])

@shop_router.message(F.text == 'Куртки')
async def jackets(message: types.Message):
    jackets1 = get_product_by_category(4)
    kb = ReplyKeyboardRemove()
    await message.answer('Коллекция курток в нашем магазине:', reply_markup=kb)
    for j in jackets1:
        await message.answer(j[1])

@shop_router.message(F.text == 'Оформить заказ')
async def order(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer(order_text, reply_markup=kb)
