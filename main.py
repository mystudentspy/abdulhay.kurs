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
# from handlers.delete import rt as delete
from handlers.photo import rt as photo
from handlers.forward import rt as forward
from handlers.reply import rt as reply
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
    # dp.include_router(delete)
    dp.include_router(photo)
    dp.include_router(forward)
    dp.include_router(reply)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("dasturni to'xtatdingiz!")