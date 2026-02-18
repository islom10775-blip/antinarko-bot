import os
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

keyboard = [["🚫 Anti Narko", "❓ Muammolar va Savollar"]]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum!\nQanday xizmat kerak?",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚫 Anti Narko":
        await update.message.reply_text(
            "Iltimos:\n1. Batafsil ma'lumot\n2. Rasm\n3. Telefon raqam\n4. Maktab raqami\n\nYuboring."
        )
        return

    if text == "❓ Muammolar va Savollar":
        await update.message.reply_text(
            "Iltimos:\n1. Muammo yoki savolingiz\n2. Telefon raqam\n3. Maktab raqami\n\nYuboring."
        )
        return

    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, handle_message))

app.run_polling()
