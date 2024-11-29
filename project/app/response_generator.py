"""Response generator module"""
from .responses import greeting, product, support

class ResponseGenerator:
    def __init__(self):
        self.response_handlers = {
            'greeting': greeting.get_greeting_response,
            'product': product.get_product_response,
            'issue': support.get_support_response,
            'help': support.get_support_response,
        }

    def generate_response(self, intent, message=None):
        """Generate appropriate response based on intent"""
        try:
            handler = self.response_handlers.get(intent)
            if handler:
                return handler()
            return "I understand. How can I assist you further?"
        except Exception as e:
            return "I'm here to help. What can I do for you?"