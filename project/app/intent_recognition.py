"""Intent recognition module"""
import re
import logging

logger = logging.getLogger(__name__)

class IntentRecognizer:
    def __init__(self):
        self.intents = {
            'greeting': r'\b(hello|hi|hey|good\s*(morning|afternoon|evening))\b',
            'farewell': r'\b(bye|goodbye|see\s*you|take\s*care)\b',
            'help': r'\b(help|support|assist|guidance)\b',
            'product': r'\b(product|pricing|features|service)\b',
            'issue': r'\b(problem|issue|error|not\s*working)\b'
        }
        self.intent_patterns = {
            intent: re.compile(pattern, re.IGNORECASE) 
            for intent, pattern in self.intents.items()
        }

    def recognize_intent(self, message):
        if not message:
            return 'general'
            
        message = message.lower()
        for intent, pattern in self.intent_patterns.items():
            if pattern.search(message):
                return intent
        return 'general'