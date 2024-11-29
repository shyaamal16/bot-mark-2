from .intent_recognition import IntentRecognizer
from .response_generator import ResponseGenerator
from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class ChatManager:
    def __init__(self):
        try:
            self.sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
            self.intent_recognizer = IntentRecognizer()
            self.response_generator = ResponseGenerator()
        except Exception as e:
            logger.error(f"Error initializing chat manager: {e}")
            raise

    def handle_message(self, message, user_data):
        try:
            if not message:
                return "I didn't receive any message. How can I help you?"

            # Log incoming message
            logger.info(f"Received message from {user_data.get('visitor_id')}: {message}")

            # Analyze sentiment
            sentiment = self.sentiment_analyzer(message)[0]
            logger.info(f"Sentiment analysis: {sentiment}")

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