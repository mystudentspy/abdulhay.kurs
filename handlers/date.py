from aiogram import filters, types, Router
import datetime
rt = Router()
@rt.message(filters.Command("soat"))
async def data(msg: types.Message):
    n = msg.date + datetime.timedelta(hours=5)
    await msg.answer(n.strftime("%H:%M:%S"))
