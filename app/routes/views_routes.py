from flask import Blueprint
from app.auth_utils import login_required
from app.controllers.auth_controller import login_view, logout_view
from app.controllers.person_controllers_views import (
    index_view,
    list_persons_view,
    create_person_view,
    edit_person_view,
    delete_person_view,
)

bp = Blueprint('views', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return login_view()


@bp.route('/logout')
def logout():
    return logout_view()


@bp.route('/')
@login_required
def index():
    return index_view()


@bp.route('/persons')
@login_required
def persons_view():
    return list_persons_view()


@bp.route('/persons/create', methods=['GET', 'POST'])
@login_required
def create_person():
    return create_person_view()


@bp.route('/persons/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_person(id):
    return edit_person_view(id)


@bp.route('/persons/delete/<int:id>', methods=['POST'])
@login_required
def delete_person(id):
    return delete_person_view(id)
