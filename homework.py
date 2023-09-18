import asyncio
import logging
from bot import bot, dp
from handlers import (
    start_router,
    info_router,
    picture_router,
    echo_router,
    shop_router,
    questions_router
)


async def homework():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(homework())