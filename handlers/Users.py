from aiogram import types, filters, Router
import datetime
rt = Router()
@rt.message(filters.Command("info"))
async def test(msg: types.Message):
    # print(msg.from_user)
    # print(msg.chat)
    # if msg.chat.type == "private":
        await msg.answer(f"bu odam ismi:  {msg.chat.first_name}")
        await msg.answer(f"bu odamning foydalanuvchi nomi:  {msg.chat.username}")
        if msg.from_user.last_name:
            await msg.answer(f"bu odamning familiyasi:  {msg.chat.last_name}")
        else:
            await msg.answer(f"bu odamning familiyasi mavjud emas!")
