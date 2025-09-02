from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

STATE1 = 1
STATE2 = 2

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Waza: dame una retroalimentacion",
        reply_markup=ReplyKeyboardMarkup([["Cancelar"]], one_time_keyboard=True)
    )
    return STATE1

async def inputFeedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    if len(texto) < 10:
        await update.message.reply_text("muy corto, por favor detalla mas tu feedback")
        return STATE1
    await update.message.reply_text("grax por tu feedback")
    return ConversationHandler.END

async def inputFeedback2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gracias por tu feedback adicional!")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Se cancelo la conversacion de feedback.")
    return ConversationHandler.END
