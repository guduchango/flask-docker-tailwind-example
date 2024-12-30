from flask import jsonify, abort
from app.models import Person
from app import db


def create_person_logic(data):
    email = data['email']
    person = Person(name=data['name'], age=data['age'], email=email)

    existing_person = Person.query.filter_by(email=email).first()
    if existing_person:
        return jsonify({"message": "duplicated email"}), 400

    db.session.add(person)
    db.session.commit()
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "email": person.email}), 201


def get_persons_logic():
    persons = Person.query.all()
    return jsonify([{"id": p.id, "name": p.name, "age": p.age, "email": p.email} for p in persons])


def update_person_logic(person_id, data):
    person = db.session.get(Person, person_id)

    if not person:
        abort(404, description="Person not found")

    person.name = data.get('name', person.name)
    person.age = data.get('age', person.age)
    person.email = data.get('email', person.email)
    db.session.commit()
    return jsonify({"id": person.id, "name": person.name, "age": person.age, "email": person.email})


def delete_person_logic(person_id):
    person = db.session.get(Person, person_id)

    if not person:
        abort(404, description="Person not found")

    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted"})