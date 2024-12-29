from functools import wraps
from flask import session, redirect, url_for, flash,jsonify,request
from app.models import User
from sqlalchemy.orm import Session
from flask_jwt_extended import decode_token
from app import db

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, inicie sesión para acceder a esta página.', 'error')
            return redirect(url_for('views.login'))
        return f(*args, **kwargs)
    return decorated_function

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"msg": "Token is missing!"}), 401

        try:
            token = token.split(" ")[1]  # Remove "Bearer " prefix
            decoded = decode_token(token)  # Decodifica el token usando Flask-JWT
            user_id = decoded["sub"]
            session = db.session
            user = session.get(User, user_id) 
            if not user:
                raise ValueError("User not found")
        except Exception as e:
            return jsonify({"msg": f"Token is invalid! {str(e)}"}), 401

        return f(*args, **kwargs)
    return decorated