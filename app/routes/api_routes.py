from flask import Blueprint, jsonify, request, abort
from ..models import Person, User
from .. import db
from flask_jwt_extended import create_access_token
from app.auth_utils import token_required


bp = Blueprint('main', __name__)

@bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    new_user = User(username=username)
    new_user.set_password('admin123')
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

@bp.route('/persons', methods=['POST'])
@token_required
def create_person():
    data = request.get_json()
    email = data['email']
    person = Person(name=data['name'], age=data['age'], email=email)

    existing_person = Person.query.filter_by(email=email).first()
    if existing_person:
            return jsonify({"message": "duplicated email"}), 400

    db.session.add(person)
    db.session.commit()
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "email": person.email}), 201

# Leer todas las personas
@bp.route('/persons', methods=['GET'])
@token_required
def get_persons():
    persons = Person.query.all()
    return jsonify([{"id": p.id, "name": p.name, "age": p.age, "email": p.email} for p in persons])

# Actualizar una persona
@bp.route('/persons/<int:person_id>', methods=['PUT'])
@token_required
def update_person(person_id):
    data = request.get_json()
    person = db.session.get(Person, person_id)
    
    if not person:
        abort(404, description="Person not found")

    person.name = data.get('name', person.name)
    person.age = data.get('age', person.age)
    person.email = data.get('email', person.email)
    db.session.commit()
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "email": person.email})

# Eliminar una persona
@bp.route('/persons/<int:person_id>', methods=['DELETE'])
@token_required
def delete_person(person_id):
    person = db.session.get(Person, person_id)
    
    if not person:
        abort(404, description="Person not found")

    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted"})