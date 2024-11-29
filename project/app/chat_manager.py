"""Chat manager module"""
import logging
from .intent_recognition import IntentRecognizer
from .response_generator import ResponseGenerator

logger = logging.getLogger(__name__)

class ChatManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChatManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        try:
            self.intent_recognizer = IntentRecognizer()
            self.response_generator = ResponseGenerator()
            self._initialized = True
        except Exception as e:
            logger.error(f"Error initializing chat manager: {e}")
            raise

    def handle_message(self, message, user_data):
        try:
            if not message:
                return "I didn't receive any message. How can I help you?"

            # Log incoming message
            logger.info(f"Received message from {user_data.get('visitor_id')}: {message}")

            # Recognize intent
            intent = self.intent_recognizer.recognize_intent(message)
            logger.info(f"Recognized intent: {intent}")

            # Generate response
            response = self.response_generator.generate_response(intent, message)
            logger.info(f"Generated response: {response}")

            return response

        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return "I apologize, but I'm having trouble processing your request. Please try again."