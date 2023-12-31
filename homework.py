import asyncio
import logging
from bot import bot, dp, scheduler
from admin_handlers.group33_3_handlers import admin_router
from handlers import (
    start_router,
    info_router,
    picture_router,
    echo_router,
    shop_router,
    questions_router,
    scheduler_router
)
from db.queries import (init_db, create_tables, products_tables, save_user, admin_id_tables)


async def on_startup(dispatcher):
    init_db()
    create_tables()
    admin_id_tables()
    products_tables()
    save_user


async def homework():
    dp.startup.register(on_startup)

    dp.include_router(admin_router)
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    dp.include_router(scheduler_router)

    dp.include_router(echo_router)

    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(homework())