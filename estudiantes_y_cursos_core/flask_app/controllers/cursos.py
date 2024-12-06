from flask_app import app
from flask_app.models.curso import Curso
from flask import render_template, redirect, request

@app.route('/')
@app.route('/cursos')
def cursos():
    cursos = Curso.get_all()
    return render_template("cursos.html", cursos=cursos)

@app.route('/cursos/crear', methods=['POST'])
def cursos_crear():
    datos={
        "nombre": request.form['nombre']
    }
    Curso.save(datos)
    return redirect('/cursos')

@app.route('/cursos/<int:id>')
def mostrar_curso(id):
    datos={
        "id":id
    }
    curso=Curso.get_cursos_y_estudiantes(datos)
    return render_template("mostrar_curso.html", curso=curso)