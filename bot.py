from telegram.ext import Application, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters
from handlers import commands, feedback, rating

def main():
    app = Application.builder().token("8011967782:AAF4lZG3fOGwiEczgz0Sq2mhN-_ma5s1zxM").build()

    # Comandos simples
    app.add_handler(CommandHandler("start", commands.welcome))
    app.add_handler(CommandHandler("nota", rating.askForNota))
    app.add_handler(CommandHandler("humor", rating.humor))  
    app.add_handler(CommandHandler("cancel", commands.cancel))  

    # Conversación de feedback
    feedback_handler = ConversationHandler(
        entry_points=[CommandHandler("feedback", feedback.feedback)],
        states={
            feedback.STATE1: [MessageHandler(filters.TEXT & ~filters.COMMAND, feedback.inputFeedback)],
            feedback.STATE2: [MessageHandler(filters.TEXT & ~filters.COMMAND, feedback.inputFeedback2)],
        },
        fallbacks=[CommandHandler("cancel", feedback.cancel)],
    )
    app.add_handler(feedback_handler)

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
