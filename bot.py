from telegram.ext import Application, CommandHandler, ConversationHandler
from handlers import commands, feedback, rating, support
from config.settings import TOKEN
import logging

def main():
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    
    # Crear aplicación
    app = Application.builder().token(TOKEN).build()
    
    # Comandos básicos
    app.add_handler(CommandHandler("start", commands.start))
    app.add_handler(CommandHandler("help", commands.help_command))
    app.add_handler(CommandHandler("about", commands.about))
    app.add_handler(CommandHandler("stats", commands.stats))
    
    # Conversaciones
    app.add_handler(feedback.get_conversation_handler())
    app.add_handler(rating.get_conversation_handler())
    app.add_handler(support.get_conversation_handler())
    
    # Callbacks
    app.add_handler(rating.get_callback_handler())
    
    # Iniciar bot
    print("🚀 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()