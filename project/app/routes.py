from flask import Blueprint, request, jsonify, current_app
from .utils import ChatManager

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        data = request.json
        chat_manager = ChatManager()
        
        # Extract message from Zoho SalesIQ payload
        message = data.get('message', {}).get('content', '')
        visitor = data.get('visitor', {})
        
        user_data = {
            'visitor_id': visitor.get('id'),
            'name': visitor.get('name'),
            'email': visitor.get('email')
        }
        
        # Process message and generate response
        response = chat_manager.handle_message(message, user_data)
        
        return jsonify({
            'status': 'success',
            'response': response
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500