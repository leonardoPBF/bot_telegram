import requests
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Update
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

STATE1 = 1
STATE2 = 2

# Comando /start
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        first_name = update.effective_user.first_name
        message = f'Olá, {first_name}!'
        await update.message.reply_text(message)
    except Exception as e:
        print(str(e))

# Comando /feedback
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        message = 'Por favor, digite um feedback para o nosso tutorial:'
        await update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
        return STATE1
    except Exception as e:
        print(str(e))

# Entrada de feedback
async def inputFeedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = """Seu feedback foi muito curtinho... 
\nInforma mais pra gente, por favor?"""
        await update.message.reply_text(message)
        return STATE1
    else:
        message = "Muito obrigada pelo seu feedback!"
        await update.message.reply_text(message)
        return ConversationHandler.END

# Entrada alternativa
async def inputFeedback2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    feedback = update.message.text
    message = "Muito obrigada pelo seu feedback!"
    await update.message.reply_text(message)
    return ConversationHandler.END

# Comando /nota
async def askForNota(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        question = 'Qual nota você dá para o tutorial?'
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("👎 1", callback_data='1'),
             InlineKeyboardButton("2", callback_data='2'),
             InlineKeyboardButton("🤔 3", callback_data='3'),
             InlineKeyboardButton("4", callback_data='4'),
             InlineKeyboardButton("👍 5", callback_data='5')]
        ])
        await update.message.reply_text(question, reply_markup=keyboard)
    except Exception as e:
        print(str(e))

# Resposta ao botão
async def getNota(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()
        nota = query.data
        print(nota)
        message = f'Obrigada pela sua nota: {nota}'
        await query.message.reply_text(message)
    except Exception as e:
        print(str(e))

# Cancelar conversa
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return ConversationHandler.END

# Função principal
def main():
    token = '8011967782:AAF4lZG3fOGwiEczgz0Sq2mhN-_ma5s1zxM'
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('feedback', feedback)],
        states={
            STATE1: [MessageHandler(filters.TEXT & ~filters.COMMAND, inputFeedback)],
            STATE2: [MessageHandler(filters.TEXT & ~filters.COMMAND, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    app.add_handler(conversation_handler)

    app.add_handler(CommandHandler('nota', askForNota))
    app.add_handler(CallbackQueryHandler(getNota))

    print("Bot rodando com Application (v22.3)...")
    app.run_polling()

if __name__ == "__main__":
    main()
