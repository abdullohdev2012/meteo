from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



async def start_menu():
    btn = ReplyKeyboardMarkup( resize_keyboard=True)
    btn.add(

    

    )
    btn.row("☀️погода сейчас","🔮 На 5 дней")
    btn.row("🌅 На завтра","🔮 На 10 дней")
    btn.row("🔔 Уведомления")
    btn.row("⚙️ Настройки")
    return btn

async def start_t():
    btn = ReplyKeyboardMarkup( resize_keyboard=True)
    btn.add(

    

    )
    btn.row("🌍 изменить город")
    btn.row("📏единитцы измерения","🇷🇺/🇬🇧 язык")
    btn.row("👥добавить бота на канал/группу")
    btn.row("🔙назад")
    return btn

   
