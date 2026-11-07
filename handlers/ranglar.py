from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("COLORS"))
async def colors_handler(msg: types.Message):
    await msg.answer("oq rang")
    await msg.answer("sariq rang")
    await msg.answer("qizil rang")
    await msg.answer("ko'k rang")
