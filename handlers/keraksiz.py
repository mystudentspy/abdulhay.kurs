from aiogram import types, filters, Router
rt = Router()
@rt.message()
async def test_hand(msg: types.Message):
    print()
    if msg.new_chat_members:
        ism = msg.new_chat_members[0].first_name
        if msg.from_user.id != msg.new_chat_members[0].id:
            await msg.answer(f"guruhga {ism} ni \n{msg.from_user.first_name} qo'shdi")
        else:
            await msg.answer(f"{ism} guruhga xush kelib siz")
    elif msg.left_chat_member:
        ism = msg.left_chat_member.first_name
        if msg.from_user.id != msg.left_chat_member.id:
            await msg.answer(f"{ism} ni \n{msg.from_user.first_name} guruhdan chiqarib tashladi")
        else:
            await msg.answer(f"{ism} guruhdan chiqib ketdi")
    elif msg.delete_chat_photo:
        ism = msg.from_user.first_name
        if msg.from_user.id != msg.delete_chat_photo:
            await msg.answer(f"{ism} guruhning rasmini ochirib tashladi")
    elif msg.new_chat_title:
        ism = msg.from_user.first_name
        if msg.from_user.id != msg.new_chat_title:
            await msg.answer(f"{ism} guruhning nomini o'zgartirdi")
    elif msg.new_chat_photo:
        ism = msg.from_user.first_name
        if msg.from_user.id != msg.new_chat_photo:
            await msg.answer(f"{ism} guruhning rasmini o'zgartirdi")

