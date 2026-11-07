from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("salom"))
async def reply(msg: types.Message):
    await msg.reply("nima gap")
