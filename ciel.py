import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hi how i can help you?")
async def handle_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.animation:
        await update.message.reply_animation("https://64.media.tumblr.com/54f0a2bf618375fd894b64c25058e246/cff4ac0c71fd143c-e1/s500x750/582e7f1e4a31e50d521cd8b77a89363454a2ee2a.gifv")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if text == "hi":
        await update.message.reply_text("hi how are you?")
    elif text == "bye":
        await update.message.reply_text("bye")
    else:
        await update.message.reply_text("under develop")
def main() -> None:
    application = Application.builder().token("bot token").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.ANIMATION, handle_gif))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()
