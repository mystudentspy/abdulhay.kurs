from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("help"))
async def help_handler(msg: types.Message):
    await msg.answer("qanday yordam kerak")

