from aiogram import types, Router, F
from bot import bot
import sqlite3
from pathlib import Path


admin_router = Router()

conn = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
cursor = conn.cursor()

forbidden_words = ['мефисто', 'альтрон', 'апокалипсис', 'галактус', 'танос']

@admin_router.message((F.chat.type != 'private') & (F.text))
async def word(message: types.Message):
    for w in forbidden_words:
        if w in message.text.lower():
            await message.answer('Такие слова запрещены')
            break
    cursor.execute('SELECT adminid FROM admin_id')
    if cursor.fetchone() is None:
        user = message.reply_to_message.from_user.id
        await message.answer('Вы получаете "BAN" за использование запрещённых слов')
        await bot.ban_chat_member(message.chat.id, user)
        await message.delete()
    else:
        await message.answer('Замечание за отправку запрещённых слов')
        await message.delete()
