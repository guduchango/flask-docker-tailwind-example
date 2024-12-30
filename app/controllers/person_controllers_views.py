from flask import render_template, flash, redirect, url_for, request, abort
from app.models import Person
from app import db


def index_view():
    return render_template('index.html', title="Página Principal")


def list_persons_view():
    persons = Person.query.all()
    return render_template('persons/index_person.html', title="Lista de Personas", persons=persons)


def create_person_view():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        email = request.form['email']

        existing_person = Person.query.filter_by(email=email).first()
        if existing_person:
            flash('El correo electrónico ya está registrado con otra persona.', 'error')
            return redirect(url_for('views.create_person'))

        person = Person(name=name, age=age, email=email)
        db.session.add(person)
        db.session.commit()
        flash('Persona creada con éxito.', 'success')
        return redirect(url_for('views.persons_view'))

    return render_template('persons/create_person.html', title="Crear Persona")


def edit_person_view(id):
    person = db.session.get(Person, id)
    if not person:
        abort(404, description="Person not found")

    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        email = request.form['email']

        existing_person = Person.query.filter_by(email=email).first()
        if existing_person and existing_person.id != id:
            flash('El correo electrónico ya está registrado con otra persona.', 'error')
            return redirect(url_for('views.edit_person', id=id))

        person.name = name
        person.age = age
        person.email = email
        db.session.commit()
        flash('Persona actualizada con éxito.', 'success')
        return redirect(url_for('views.persons_view'))

    return render_template('persons/edit_person.html', title="Editar Persona", person=person)


def delete_person_view(id):
    person = db.session.get(Person, id)
    if not person:
        abort(404, description="Person not found")
    db.session.delete(person)
    db.session.commit()
    flash('Persona eliminada con éxito.', 'success')
    return redirect(url_for('views.persons_view'))