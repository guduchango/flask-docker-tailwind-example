from flask import Blueprint, request
from app.auth_utils import token_required
from app.controllers.auth_controller import register_user_logic, login_user_logic
from app.controllers.person_controller import (
    create_person_logic,
    get_persons_logic,
    update_person_logic,
    delete_person_logic,
)

bp = Blueprint('api', __name__)

# Auth Routes
@bp.route('/register', methods=['POST'])
def register_user():
    return register_user_logic(request.json)


@bp.route('/login', methods=['POST'])
def login_user():
    return login_user_logic(request.json)


# Person Routes
@bp.route('/persons', methods=['POST'])
@token_required
def create_person():
    return create_person_logic(request.json)


@bp.route('/persons', methods=['GET'])
@token_required
def get_persons():
    return get_persons_logic()


@bp.route('/persons/<int:person_id>', methods=['PUT'])
@token_required
def update_person(person_id):
    return update_person_logic(person_id, request.json)


@bp.route('/persons/<int:person_id>', methods=['DELETE'])
@token_required
def delete_person(person_id):
    return delete_person_logic(person_id)