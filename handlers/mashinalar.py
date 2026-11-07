from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("CARS"))
async def cars_handler(msg: types.Message):
    await msg.answer("cobalt")
    await msg.answer("gentra")
    await msg.answer("malibu")
    await msg.answer("spark")
