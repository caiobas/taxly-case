from flask import request, abort
from config import Config

def authenticate_request():
    token = request.headers.get('Authorization')

    if not token or token != f'Bearer {Config.SECRET_KEY}':
        abort(401, 'Unauthorized: Invalid token')