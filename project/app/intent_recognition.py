from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class IntentRecognizer:
    def __init__(self):
        self.intents = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'farewell': ['bye', 'goodbye', 'see you', 'take care'],
            'help': ['help', 'support', 'assist', 'guidance'],
            'product': ['product', 'pricing', 'features', 'service'],
            'issue': ['problem', 'issue', 'error', 'not working']
        }

    def recognize_intent(self, message):
        message = message.lower()
        for intent, keywords in self.intents.items():
            if any(keyword in message for keyword in keywords):
                return intent
        return 'general'