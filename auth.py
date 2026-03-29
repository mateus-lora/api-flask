from functools import wraps
from flask import request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("ERRO: Variável de ambiente API_KEY não foi configurada no arquivo .env!")

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('x-api-key') == API_KEY:
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "Não autorizado. Forneça um x-api-key válido no header."}), 401
    return decorated_function