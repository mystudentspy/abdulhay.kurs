from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("FRUITS"))
async def fruits_handler(msg: types.Message):
    await msg.answer("olma")
    await msg.answer("banan")
    await msg.answer("apelsin")
    await msg.answer("nok")
