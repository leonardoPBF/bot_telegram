import json
import os
from datetime import datetime
from config.settings import Config

def load_json_file(filepath):
    """Cargar archivo JSON"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_json_file(filepath, data):
    """Guardar archivo JSON"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_feedback(user_id, feedback_text):
    """Guardar feedback en archivo"""
    feedbacks = load_json_file(Config.FEEDBACK_FILE)
    
    feedback_data = {
        'user_id': user_id,
        'text': feedback_text,
        'timestamp': datetime.now().isoformat(),
        'length': len(feedback_text)
    }
    
    if str(user_id) not in feedbacks:
        feedbacks[str(user_id)] = []
    
    feedbacks[str(user_id)].append(feedback_data)
    save_json_file(Config.FEEDBACK_FILE, feedbacks)

def get_user_data(user_id):
    """Obtener datos del usuario"""
    users = load_json_file(Config.DATA_FILE)
    return users.get(str(user_id), {})