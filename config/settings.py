import os
from dataclasses import dataclass

# Token del bot
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8011967782:AAF4lZG3fOGwiEczgz0Sq2mhN-_ma5s1zxM")

# Estados de conversación
@dataclass
class States:
    WAITING_FEEDBACK = 1
    WAITING_RATING_COMMENT = 2
    WAITING_SUPPORT = 3

# Configuración básica
@dataclass  
class Config:
    MAX_FEEDBACK_LENGTH = 500
    MIN_FEEDBACK_LENGTH = 10
    DATA_FILE = "data/users.json"
    FEEDBACK_FILE = "data/feedback.json"
    LOG_FILE = "data/logs.txt"