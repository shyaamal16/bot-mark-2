from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class ChatManager:
    def __init__(self):
        try:
            self.sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        except Exception as e:
            logger.error(f"Error initializing sentiment analyzer: {e}")
            self.sentiment_analyzer = None

    def handle_message(self, message, user_data):
        try:
            # Analyze sentiment if analyzer is available
            sentiment = None
            if self.sentiment_analyzer:
                sentiment = self.sentiment_analyzer(message)[0]
            
            # Basic response logic
            response = self.generate_response(message, sentiment)
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return "I apologize, but I'm having trouble processing your request. Please try again."

    def generate_response(self, message, sentiment=None):
        # Simple response logic - can be enhanced based on requirements
        message = message.lower()
        
        if "hello" in message or "hi" in message:
            return "Hello! How can I assist you today?"
        elif "help" in message:
            return "I'm here to help! Please let me know what you need assistance with."
        elif "bye" in message:
            return "Goodbye! Have a great day!"
        else:
            return "I understand your message. How can I help you further?"