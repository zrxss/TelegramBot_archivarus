import  asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

import os

from config import TOKEN, TG_PROXY

import database
from handlers.private_chat import private_router
from handlers.group_parser import group_router


session = AiohttpSession(proxy=TG_PROXY)

ruz_bot = Bot(token=TOKEN, session=session)

dp=Dispatcher()



async def main():
    database.create_table()
    if not os.path.exists("failed_file"):
        os.makedirs("failed_file")
    dp.include_router(group_router)
    dp.include_router(private_router)
    await dp.start_polling(ruz_bot)

if __name__ == '__main__':
    asyncio.run(main())