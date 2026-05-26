from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from gtts import gTTS
import os

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing!")


menu = ReplyKeyboardMarkup(
    [
        ["🇬🇧 Урок дня", "🎧 Произношение"],
        ["📝 Мини-тест", "📈 Прогресс"],
        ["ℹ️ О Bekha English"]
    ],
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🇬🇧 Добро пожаловать в Bekha English!

Учим английский вместе — просто и бесплатно 🚀

Каждый день:
✅ Слово дня
✅ Полезная фраза
✅ Произношение
✅ Мини-тест

Сегодня всего 5 минут английского 💪
"""

    await update.message.reply_text(text, reply_markup=menu)


async def lesson(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🇬🇧 Bekha English — День 1

📌 Слово дня

Work — работа

🗣 Произношение:
[wɜːrk]

Пример:
I work every day.
— Я работаю каждый день.

━━━━━━━━━━━━━━

🗣 Фраза дня

I want to improve my English.
— Я хочу улучшить свой английский.

🎧 Повтори 3 раза вслух.

━━━━━━━━━━━━━━

💡 Мини-правило

I want...

Примеры:

I want coffee.
— Я хочу кофе.

I want to learn English.
— Я хочу учить английский.

━━━━━━━━━━━━━━

📝 Мини-тест

Как переводится “work”?

1️⃣ Деньги
2️⃣ Работа ✅
3️⃣ Документы

━━━━━━━━━━━━━━

🔥 Мини-практика

Как сказать:
«Я хочу работать»?

Ответ:
I want to work.

📈 Прогресс:
Day 1 / 100
"""

    await update.message.reply_text(text)


async def pronunciation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrase = "I want to improve my English"

    tts = gTTS(text=phrase, lang="en")

    filename = "voice.mp3"
    tts.save(filename)

    with open(filename, "rb") as audio:
        await update.message.reply_audio(audio)

    os.remove(filename)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bekha English 🇬🇧\n\n"
        "Учим английский вместе — просто и бесплатно 🚀"
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lesson", lesson))
    app.add_handler(CommandHandler("speak", pronunciation))
    app.add_handler(CommandHandler("about", about))

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
