from flask import Blueprint, jsonify, request
from ..models import Person
from .. import db

bp = Blueprint('main', __name__)

# Crear una nueva persona
@bp.route('/persons', methods=['POST'])
def create_person():
    data = request.get_json()
    person = Person(name=data['name'], age=data['age'], email=data['email'])

    db.session.add(person)
    db.session.commit()
    return jsonify({"message": "Person created", "person": {"id": person.id, "name": person.name, "age": person.age, "email": person.email}}), 201

# Leer todas las personas
@bp.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify([{"id": p.id, "name": p.name, "age": p.age, "email": p.email} for p in persons])

# Actualizar una persona
@bp.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.get_json()
    person = Person.query.get_or_404(person_id)
    person.name = data.get('name', person.name)
    person.age = data.get('age', person.age)
    person.email = data.get('email', person.email)
    db.session.commit()
    return jsonify({"message": "Person updated", "person": {"id": person.id, "name": person.name, "age": person.age, "email": person.email}})

# Eliminar una persona
@bp.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted"})