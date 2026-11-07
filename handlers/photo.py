from aiogram import Router, types, filters
rt = Router()
rasmlar = [
    "https://www.facebook.com/groups/2441757829347254/posts/2972902666232765/",
    "https://www.mehmetuzumakademi.com/blog/manzara-fotografi-nasil-cekilir",
    "https://blog.tatilsepeti.com/genel/doya-doya-manzara-fotografi-cekebileceginiz-kentler/"
]
@rt.message(filters.Command("photo"))
async def photo(msg: types.Message):
    await msg.answer_photo(rasmlar[0])
    await msg.answer_photo(rasmlar[1])
    await msg.answer_photo(rasmlar[2])
