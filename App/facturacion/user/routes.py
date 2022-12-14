from flask import Blueprint, request, jsonify

user = Blueprint('user', __name__)


@user.route('/create_user', methods=['GET', 'POST'])
def create_user_endpoint() -> dict:
    '''Sends a POST request to create a new user'''
    return jsonify({'message': 'User created successfully!'})
