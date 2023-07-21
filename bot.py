import logging
from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton
from aiogram import Bot ,Dispatcher ,executor,types
from btn import start_menu,start_t
from keyboards import my_inline_btn,my_inline_btn_bot


logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5898062021:AAHAbZyGXdZqxPWIGiOx_BTJPc6v1OG-55A"

bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_bot(message:types.Message):
    btn = await start_menu()
    await message.answer("Вот список того, что я умею:", reply_markup=btn)

@dp.message_handler(text=["☀️погода сейчас"])
async def pogoda_bot(message:types.Message):
    bots = await my_inline_btn()
    rasm = types.InputFile("rasm.jpg")
    await message.answer_photo(photo=rasm, caption="Bu Odilning rasmi",reply_markup=bots)

@dp.message_handler(text=["🔮 На 5 дней"])
async def pooda_bot(message:types.Message):
    bots = await my_inline_btn()
    rasm = types.InputFile("rasm.jpg")
    await message.answer_photo(photo=rasm, caption="Bu Odilning rasmi",reply_markup=bots)


@dp.message_handler(text=["🌅 На завтра"])
async def pgoda_bot(message:types.Message):
    bots = await my_inline_btn()
    rasm = types.InputFile("rasm.jpg")
    await message.answer_photo(photo=rasm, caption="Bu Odilning rasmi",reply_markup=bots)



@dp.message_handler(text=["🔮 На 10 дней"])
async def ogoda_bot(message:types.Message):
    bots = await my_inline_btn()
    rasm = types.InputFile("rasm.jpg")
    await message.answer_photo(photo=rasm, caption="Bu Odilning rasmi",reply_markup=bots)    


  
@dp.message_handler(text=["🔔 Уведомления"])
async def pogod_bot(message:types.Message):
    bots = await my_inline_btn_bot()
    await message.answer("Выберите время отправки уведомлений Прогноз на сегодня",reply_markup=bots)  

@dp.message_handler(text=["⚙️ Настройки"])
async def pogoa_bot(message:types.Message):
    bots = await start_t()
    await message.answer("настройки",reply_markup=bots)  
    
@dp.message_handler(text=["🔙назад"])
async def pogoda_bot(message:types.Message):
    btns = await start_menu()
    await message.answer("mana",reply_markup=btns)

if __name__ == "__main__":
    executor.start_polling(dp)
