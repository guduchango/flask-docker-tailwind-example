from flask import Blueprint, render_template, request, redirect, url_for, flash,session,abort
from ..models import Person
from app.models import User
from .. import db
from app.auth_utils import login_required

bp = Blueprint('views', __name__)   

@bp.route('/login', methods=['GET', 'POST'])
def login():
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

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Sesión cerrada.', 'success')
    return redirect(url_for('views.login'))

# Página principal
@bp.route('/')
@login_required
def index():
    return render_template('index.html', title="Página Principal")

# Lista de personas
@bp.route('/persons')
@login_required
def persons_view():
    persons = Person.query.all()
    return render_template('persons/index_person.html', title="Lista de Personas", persons=persons)

# Crear una persona
@bp.route('/persons/create', methods=['GET', 'POST'])
@login_required
def create_person():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']

        existing_person = Person.query.filter_by(email=email).first()
        if existing_person:
            flash('El correo electrónico ya está registrado con otra persona.', 'error')
            return redirect(url_for('views.create_person'))

        person = Person(name=name, age=int(age), email=email)
        db.session.add(person)
        db.session.commit()
        flash('Persona creada con éxito.', 'success')
        return redirect(url_for('views.persons_view'))

    return render_template('persons/create_person.html', title="Crear Persona")

# Editar una persona
@bp.route('/persons/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_person(id):
    person = db.session.get(Person, id)
    if not person:
        abort(404, description="Person not found")
    
    if request.method == 'POST':
        email = request.form['email']
        person.name = request.form['name']
        person.age = int(request.form['age'])
        person.email = email

         # Verificar si el email ya pertenece a otra persona
        existing_person = Person.query.filter_by(email=email).first()
        if existing_person and existing_person.id != id:
            flash('El correo electrónico ya está registrado con otra persona.', 'error')
            return redirect(url_for('views.edit_person', id=id))


        db.session.commit()
        flash('Persona actualizada con éxito.', 'success')
        return redirect(url_for('views.persons_view'))

    return render_template('persons/edit_person.html', title="Editar Persona", person=person)

# Borrar una persona
@bp.route('/persons/delete/<int:id>', methods=['POST'])
@login_required
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    flash('Persona eliminada con éxito.', 'success')
    return redirect(url_for('views.persons_view'))