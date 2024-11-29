from flask import Blueprint, request, jsonify, current_app
from .utils import ChatManager
import logging

logger = logging.getLogger(__name__)

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        data = request.json
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'No data received'
            }), 400

        chat_manager = ChatManager()
        
        # Extract message from Zoho SalesIQ payload
        message_data = data.get('message', {})
        visitor = data.get('visitor', {})
        
        message = message_data.get('content', '')
        user_data = {
            'visitor_id': visitor.get('id'),
            'name': visitor.get('name'),
            'email': visitor.get('email')
        }
        
        # Process message and generate response
        response = chat_manager.handle_message(message, user_data)
        
        # Format response for Zoho SalesIQ
        return jsonify({
            'status': 'success',
            'response': {
                'message': response,
                'type': 'text'
            }
        }), 200
        
    except Exception as e:
        logger.error(f"Error in webhook handler: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500