from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("info"))
async def info_handler(msg: types.Message):
    await msg.answer("/COLORS")
    await msg.answer("/CARS")
    await msg.answer("/FRUITS")
    await msg.answer("/LAPTOTS")
