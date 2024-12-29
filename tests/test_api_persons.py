import json
from faker import Faker
fake = Faker()
email = fake.email()
from app.models import Person,User
from flask_jwt_extended import create_access_token

def test_user_existence(client):
    assert User.query.filter_by(username="testuser").first() is not None

def test_get_all_persons(client,general_token):
    response = client.get(
        '/api/persons',
        headers={"Authorization": f"Bearer {general_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_person(client,general_token):
    payload = {"name": fake.name(), "age":fake.random_int(18,60), "email": email}
    response = client.post(
        '/api/persons', 
        headers={"Authorization": f"Bearer {general_token}"},
        json=payload
        )
    assert response.status_code == 201
    assert response.json["email"] == email

def test_create_person_duplicate_email(client,general_token):
    payload = {"name": fake.name(), "age":fake.random_int(18,60), "email": email}
    response = client.post(
        '/api/persons', 
        headers={"Authorization": f"Bearer {general_token}"},
        json=payload
        )
    assert response.status_code == 400 

def test_update_person(client,general_token):
    person = Person.query.filter_by(email=email).first()
    update_payload = {"name": fake.name()}
    response = client.put(
            f"/api/persons/{person.id}",
            headers={"Authorization": f"Bearer {general_token}"},
            json=update_payload
        )
    assert response.status_code == 200
    assert response.json["name"] == person.name

def test_delete_person(client,general_token):
    person = Person.query.filter_by(email=email).first()
    response = client.delete(
            f'/api/persons/{person.id}',
            headers={"Authorization": f"Bearer {general_token}"},
        )
    assert response.status_code == 200

