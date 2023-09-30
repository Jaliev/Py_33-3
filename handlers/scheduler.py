from aiogram import Router, types
from aiogram.filters import Command
from bot import scheduler
from db.queries import send_reminder
from text import remind_text


scheduler_router = Router()

@scheduler_router.message(Command('remind'))
async def on_startup(message: types.Message):
    scheduler.add_job(
        send_reminder,
        "cron",
        year=2023,
        day_of_week="mon,thu, sat",
        hour=13,
        minute=45,
        second=0,
        args=(message.from_user.id,)
    )
    await message.answer(remind_text)

