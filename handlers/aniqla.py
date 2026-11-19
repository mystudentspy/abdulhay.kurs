from aiogram import types, filters, Router
# import datetime
rt = Router()
@rt.message(filters.Command("aniqla"))
async def aniqla(msg: types.Message):
    # print(msg.from_user)
    # print(msg.chat)
    # if msg.chat.type == "private":
    if msg.from_user.username:
        await msg.answer(f"bu odamning user_nami:  @{msg.chat.username}")
    else:
        await msg.answer(f"bu odamning foydalanuvchi nomi:  {msg.chat.first_name}")
        # if msg.from_user.last_name:
        #     await msg.answer(f"bu odamning familiyasi:  {msg.chat.last_name}")
        # else:
        #     await msg.answer(f"bu odamning familiyasi mavjud emas!")