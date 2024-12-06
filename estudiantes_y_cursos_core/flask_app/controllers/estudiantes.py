from flask_app import app
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso
from flask import render_template, redirect, request

@app.route('/estudiantes/nuevo')
def nuevo_estudiante():
    cursos = Curso.get_all()
    print(cursos)
    return render_template('nuevo_estudiante.html', cursos = cursos)

@app.route('/estudiantes/guardar', methods=['POST'])
def guardar_estudiante():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso_id']
    }
    Estudiante.crear(data)
    return redirect('/')