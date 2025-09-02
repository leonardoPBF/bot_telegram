from telegram import Update
from telegram.ext import ContextTypes

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name
    await update.message.reply_text(f"Saludinhos, {first_name}! bienvenido activa los comandos /feedback, /nota y /humor")

async def waza(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name
    await update.message.reply_text(f"Wazaaaaaaaaaaaaaaaaaaaa, {first_name}! como va todo?")
