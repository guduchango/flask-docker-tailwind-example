from flask import jsonify, request,session, flash, redirect, url_for, render_template
from app.models import User
from app import db
from flask_jwt_extended import create_access_token

"""
Api logic
"""
def register_user_logic(data):
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


def login_user_logic(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

"""
Views logic
"""
def login_view():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('views.persons_view'))
        else:
            flash('Credenciales inválidas.', 'error')
    return render_template('login.html', title='Iniciar Sesión')


def logout_view():
    session.pop('user_id', None)
    flash('Sesión cerrada.', 'success')
    return redirect(url_for('views.login'))