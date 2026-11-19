from aiogram import filters, types, Router
import datetime

from aiogram.methods import answer_guest_query

rt = Router()
@rt.message(filters.Command("soat"))
async def data(msg: types.Message):
    n = msg.date + datetime.timedelta(hours=5)
    await msg.answer(n.strftime("%H:%M:%S"))
@rt.message(filters.Command("sana"))
async def data(msg: types.Message):
    await msg.answer("")
