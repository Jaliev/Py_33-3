from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from text import start_text
from handlers.about_us import text


start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/Wildberriesshop'),
                InlineKeyboardButton(text='Telegram', url='https://t.me/wildberriesru_official'),
            ],
            [
                InlineKeyboardButton(text='Наш сайт', url='https://global.wildberries.ru/?yandex-source=desktop-maps'),
                InlineKeyboardButton(text='О нас', callback_data='about us'),
            ]
        ]
    )
    await message.answer(start_text, reply_markup=kb)

@start_router.callback_query(F.data == 'about us')
async def about(callback: types.CallbackQuery):
    await callback.message.answer(text)