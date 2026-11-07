from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer("botimiz haqida batafsil malumot uchun /info ni bosing!")

