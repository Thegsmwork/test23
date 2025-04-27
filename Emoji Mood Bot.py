from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Emoji mood dictionary
emoji_moods = {
    "😎": "Boss mode activated! 🔥",
    "😂": "Laughing out loud! 😂 Stay happy!",
    "😭": "Aww, don't cry! 🌈 Better days are coming.",
    "😡": "Take a deep breath! 😌",
    "❤️": "Love is in the air! 💕",
    "🤔": "Thinking hard? 🤓 Brain boost incoming!"
}

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    mood = emoji_moods.get(text, "Hmm, interesting emoji! 😄 Stay awesome!")
    await update.message.reply_text(mood)

# Main section
if __name__ == '__main__':
    app = ApplicationBuilder().token("8103027192:AAF4Ax458fmdyrdoFWzgIK3u78n4NE7gByM").build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running 🚀")
    app.run_polling()
