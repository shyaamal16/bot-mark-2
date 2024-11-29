class ResponseGenerator:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I assist you today?",
                "Hi there! Welcome to our service. How may I help you?"
            ],
            'farewell': [
                "Goodbye! Have a great day!",
                "Thank you for chatting with us. Take care!"
            ],
            'help': [
                "I'm here to help! What do you need assistance with?",
                "I'll be happy to help you. What's your question?"
            ],
            'product': [
                "I'd be happy to tell you about our products and services. What would you like to know?",
                "Our products are designed to meet your needs. What specific information are you looking for?"
            ],
            'issue': [
                "I'm sorry to hear you're having problems. Could you please describe the issue in detail?",
                "Let me help you resolve this issue. Can you provide more information?"
            ],
            'general': [
                "I understand. How can I assist you further?",
                "Thank you for your message. What else would you like to know?"
            ]
        }

    def generate_response(self, intent, message=None):
        responses = self.responses.get(intent, self.responses['general'])
        return responses[0]  # For simplicity, always return the first response