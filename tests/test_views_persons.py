import pytest
from flask import url_for
from app.models import User, Person
from app import db
from faker import Faker
fake = Faker()
email = fake.email()

@pytest.fixture
def authenticated_client(client):

    login_response = client.post(
        '/login', data={"username": "admin", "password": "admin123"}
    )
    
    assert login_response.status_code == 302 
    return client

def test_home_view(authenticated_client):
    response = authenticated_client.get('/')
    assert response.status_code == 200


def test_create_view_get(authenticated_client):
    response = authenticated_client.get('/persons/create')
    assert response.status_code == 200


def test_create_view_post(authenticated_client):
    data = {"name": fake.name(), "age":fake.random_int(18,60), "email": email}
    response = authenticated_client.post('/persons/create', data=data, follow_redirects=True )
    assert response.status_code == 200 
    assert b"Lista de Personas" in response.data


def test_edit_view_get(authenticated_client):
    data = {"name": fake.name(), "age":fake.random_int(18,60), "email": email}
    authenticated_client.post('/persons/create', data=data)
    person = Person.query.filter_by(email=data['email']).first()
    response = authenticated_client.get(f'/persons/edit/{person.id}')
    assert response.status_code == 200
    assert b"Editar Persona" in response.data
