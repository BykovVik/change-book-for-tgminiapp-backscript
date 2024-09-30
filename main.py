import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums.content_type import ContentType
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile


from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    webAppInfo = types.WebAppInfo(url="https://bykovvik.github.io/github-page-for-tg-change-book/")
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text='Запустить приложение', web_app=webAppInfo))
    builder.row(types.KeyboardButton(text='Наши другие проекты'))
    
    await message.answer(
        text='Добро пожаловать в приложение "Книга Перемен"! Это бесплатное приложение создано, чтобы подарить вам позитивные эмоции и развлечь. \n\nЕсли вы хотите выразить благодарность автору, вы можете ознакомиться с его каналами.\n\nКАНАЛ ДЛЯ ГИКОВ - https://t.me/this_is_for_geeks \nКАНАЛ ДЛЯ ИНДИ РАЗРАБОВ - https://t.me/gypsy_studio \n\nПодписка на них совершенно необязательна – подписывайтесь только в том случае, если вам действительно интересна эта тематика.', 
        reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: types.Message):
    data = message.web_app_data.data
    #await message.answer(data)
    photo = FSInputFile("result.jpg")
    await bot.send_photo(
        chat_id=message.chat.id, 
        photo=photo, 
        caption=data
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Если вы хотите поддержать автора, вы можете поделиться своим результатом с друзьями или в чате, а также ознакомиться с его каналами: \n\n☕️💻📱💾КАНАЛ ДЛЯ ГИКОВ - https://t.me/this_is_for_geeks \n☕️🎮🖥💽КАНАЛ ДЛЯ ИНДИ РАЗРАБОВ - https://t.me/gypsy_studio",
        disable_web_page_preview=True
    )

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
