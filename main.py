import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton("🚫 Anti Narko")
btn2 = KeyboardButton("❓ Muammolar va Savollar")
main_kb.add(btn1, btn2)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Assalomu alaykum!\nQanday xizmat kerak?", reply_markup=main_kb)

@dp.message_handler(lambda message: message.text == "🚫 Anti Narko")
async def anti_narko(message: types.Message):
    await message.answer("Iltimos:\n1. Batafsil ma'lumot\n2. Rasm\n3. Telefon raqam\n4. Maktab raqami\n\nYuboring.")

@dp.message_handler(lambda message: message.text == "❓ Muammolar va Savollar")
async def muammo(message: types.Message):
    await message.answer("Iltimos:\n1. Muammo yoki savolingiz\n2. Telefon raqam\n3. Maktab raqami\n\nYuboring.")

@dp.message_handler(content_types=['text', 'photo'])
async def forward_to_admin(message: types.Message):
    await bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
