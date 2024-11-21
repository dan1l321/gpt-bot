from dotenv import load_dotenv
import os

# Загружаем переменные из .env файла
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Далее ваш код
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я бот на основе ChatGPT. Напиши мне что-то, и я отвечу!")

async def handle_message(update: Update, context):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )
    await update.message.reply_text(response["choices"][0]["message"]["content"])

# Настройка бота
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.bot_data["httpx_client"] = {"timeout": 60}
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен!")
app.run_polling()