import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Вставь свой токен
TOKEN = "8703742383:AAGSmH9YrNbI4JkTrc1X1eon6r4Q2kkb7vM"
# Вставь ссылку, которую выдал GitHub Pages
APP_URL = "https://stanmin19-dot.github.io/my-tapper/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    builder = InlineKeyboardBuilder()
    # Создаем кнопку, которая открывает Mini App
    builder.row(types.InlineKeyboardButton(
        text="Играть в тапалку! 🐹", 
        web_app=WebAppInfo(url=APP_URL)
    ))

    await message.answer(
        f"Привет, {message.from_user.first_name}! Готов натапать на ламбу?",
        reply_markup=builder.as_markup()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())