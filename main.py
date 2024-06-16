import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router

from app.database.models import async_main


async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    print('Бот включен')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

