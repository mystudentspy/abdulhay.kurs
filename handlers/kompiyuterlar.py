from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("LAPTOTS"))
async def laptots_handler(msg: types.Message):
    await msg.answer("acer")
    await msg.answer("lenovo")
    await msg.answer("asus")
    await msg.answer("hp")
