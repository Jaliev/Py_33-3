from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton
)
from text import (
    name_text,
    age_text,
    cancel_button_text,
    cancel_text,
    tel_number_text,
    letters_text,
    numbers_text,
    tel_num_text,
    gender_text,
    gen_text,
    end_text,
    sub_is_text
)
from handlers.start import start_router
from db.queries import save_user


questions_router = Router()


class UserQuestions(StatesGroup):
    name = State()
    age = State()
    tel_number = State()
    gender = State()
    question = State()


@questions_router.message(F.text == 'Отмена')
@questions_router.message(Command('cancel'))
async def cancel_questions(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(cancel_button_text, reply_markup=ReplyKeyboardRemove())

@questions_router.message(Command('survey'))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserQuestions.name)
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отмена')]], resize_keyboard=True)
    await message.answer(name_text)
    await message.answer(cancel_text, reply_markup=kb)

@questions_router.message(F.text, UserQuestions.name)
async def process_name(message: Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer(letters_text)
    elif ' ' in message.text.strip():
        await message.answer(letters_text)
    else:
        await state.update_data(name=message.text)
        await state.set_state(UserQuestions.age)
        await message.answer(age_text)

@questions_router.message(F.text, UserQuestions.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(numbers_text)
    elif int(message.text) not in range(10, 100):
        await message.answer(numbers_text)
    else:
        await state.update_data(age=message.text)
        await state.set_state(UserQuestions.tel_number)
        await message.answer(tel_number_text)

@questions_router.message(F.text, UserQuestions.tel_number)
async def process_tel_num(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(tel_num_text)
    else:
        await state.update_data(tel=message.text)
        await state.set_state(UserQuestions.gender)
        kb = InlineKeyboardMarkup(
            inline_keyboard=
            [
                [
                 InlineKeyboardButton(text='Муж', callback_data='gen'),
                 InlineKeyboardButton(text='Жен', callback_data='gen')
                ]
            ]
        )
        await message.answer(gender_text, reply_markup=kb)
@questions_router.message(F.text, UserQuestions.gender)
async def process_gender(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    if message.text != 'Муж' or 'Жен':
        await message.answer(gen_text)
    else:
        await message.answer(end_text)
        await state.clear()

@questions_router.callback_query(F.data == 'gen')
async def gender(callback: types.CallbackQuery):
    await callback.message.answer(end_text)

@start_router.message(F.text == 'Подписаться')
async def subscribe(message: types.Message, state: FSMContext):
    await state.update_data(question=message.text)
    save_user(message.from_user.id)
    await message.answer(sub_is_text, reply_markup=ReplyKeyboardRemove())
