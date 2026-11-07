from aiogram import Router, types, filters
rt = Router()
@rt.message()
async def forward(msg: types.Message):
    # print(msg.from_user.id)
    await msg.forward(7958925525)
