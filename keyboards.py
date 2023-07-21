from aiogram import types

async def  my_inline_btn():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton("подробный прогноз",callback_data="n1"),
        types.InlineKeyboardButton("пожертвование боту",callback_data="n2"),
    )
    return btn



async def  my_inline_btn_bot():
    btn = types.InlineKeyboardMarkup(row_width=2)
    btn.add(
        types.InlineKeyboardButton("☀️прогноз на сегодня",callback_data="n1"),
        types.InlineKeyboardButton("🔮 На 5 дней",callback_data="n2"),
        types.InlineKeyboardButton("🌅 На завтра",callback_data="n1"),
        types.InlineKeyboardButton("🔮 На 10 дней",callback_data="n2"),
    )
    return btn