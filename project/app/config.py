import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    ZOHO_SALESIQ_AUTH_TOKEN = os.getenv('ZOHO_SALESIQ_AUTH_TOKEN', '')
    ZOHO_SALESIQ_PORTAL_ID = os.getenv('ZOHO_SALESIQ_PORTAL_ID', '')
    ZOHO_SALESIQ_DEPARTMENT_ID = os.getenv('ZOHO_SALESIQ_DEPARTMENT_ID', '')
    
    # AI Model Configuration
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/chatbot_model')
    INTENT_THRESHOLD = 0.7