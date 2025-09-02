from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# Comando /nota con InlineKeyboard
async def askForNota(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👎 1", callback_data='1'),
         InlineKeyboardButton("2", callback_data='2'),
         InlineKeyboardButton("🤔 3", callback_data='3'),
         InlineKeyboardButton("4", callback_data='4'),
         InlineKeyboardButton("👍 5", callback_data='5')]
    ])
    await update.message.reply_text("dame una nota, Eu acho que vou me apaxiona...", reply_markup=keyboard)

async def humor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Chiste que quieres evaluar
    chiste = "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter 🐦"

    # Opciones de reacción
    opciones = [
        "😂 Me hizo reír",
        "😐 Meh",
        "😡 Ofensivo",
        "🤯 Muy creativo",
        "😴 Aburrido"
    ]

    # Enviar el chiste
    await update.message.reply_text(f"🎭 *Chiste del día:*\n\n{chiste}", parse_mode="Markdown")

    # Enviar la encuesta
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question="¿Qué te pareció este chiste?",
        options=opciones,
        is_anonymous=False,
        allows_multiple_answers=False
    )