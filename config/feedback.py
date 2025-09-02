from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from utils.helpers import save_feedback, get_user_data
from config.settings import States
from config.messages import FEEDBACK_MESSAGES

async def start_feedback(update, context):
    """Iniciar proceso de feedback"""
    keyboard = [['❌ Cancelar']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        FEEDBACK_MESSAGES['start'], 
        reply_markup=reply_markup
    )
    return States.WAITING_FEEDBACK

async def process_feedback(update, context):
    """Procesar feedback del usuario"""
    if update.message.text == '❌ Cancelar':
        return await cancel_feedback(update, context)
    
    feedback_text = update.message.text
    user_id = update.effective_user.id
    
    # Validar longitud
    if len(feedback_text) < 10:
        await update.message.reply_text(FEEDBACK_MESSAGES['too_short'])
        return States.WAITING_FEEDBACK
    
    # Guardar feedback
    save_feedback(user_id, feedback_text)
    
    # Respuesta exitosa
    await update.message.reply_text(FEEDBACK_MESSAGES['success'])
    return ConversationHandler.END

async def cancel_feedback(update, context):
    """Cancelar feedback"""
    await update.message.reply_text("❌ Feedback cancelado.")
    return ConversationHandler.END

def get_conversation_handler():
    """Retornar handler de conversación"""
    return ConversationHandler(
        entry_points=[CommandHandler('feedback', start_feedback)],
        states={
            States.WAITING_FEEDBACK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, process_feedback)
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel_feedback)]
    )