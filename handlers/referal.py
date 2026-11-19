from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.CommandStart(deep_link=True))
async def test_handler(msg: types.Message, command: filters.CommandObject):
    ref_code = command.args
    await msg.answer(f"Ha qalesan! Seni {ref_code} taklif qildi.")

@rt.message(filters.Command("start"))
async def test_handler(msg: types.Message):
    await msg.answer(f"Ha qalesan!")
    await msg.answer("t.me/name_ismbot?start=abdulhay")
