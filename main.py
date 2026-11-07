import asyncio, logging
from aiogram import Bot, Dispatcher
from config.settings import token
from handlers.start import rt as start
from handlers.kompiyuterlar import rt as laptot
from handlers.mashinalar import rt as car
from handlers.mevalar import rt as fruit
from handlers.ranglar import rt as color
from handlers.info import rt as info
from handlers.help import rt as help
dp = Dispatcher()
async def main() :
    bot = Bot(token)
    dp.include_router(start)
    dp.include_router(info)
    dp.include_router(help)
    dp.include_router(laptot)
    dp.include_router(car)
    dp.include_router(fruit)
    dp.include_router(color)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("dasturni to'xtatdingiz!")