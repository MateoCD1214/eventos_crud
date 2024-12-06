from flask_app.models.estudiante import Estudiante
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'esquema_estudiantes_cursos'


class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        resultado = connectToMySQL(DATABASE).query_db(query)
        cursos = []
        for curso in resultado:
            cursos.append(cls(curso))
        return cursos

    @classmethod
    def save(cls, datos):
        query = "insert into cursos (nombre) values (%(nombre)s);"
        return connectToMySQL(DATABASE).query_db(query, datos)

    @classmethod
    def get_cursos_y_estudiantes(cls, datos):
        query = "select * from cursos left join estudiantes on estudiantes.curso_id = cursos.id where cursos.id = %(id)s;"
        resultados = connectToMySQL(DATABASE).query_db(query,datos)
        curso = cls(resultados[0])
        for cursox in resultados:
            datos_estudiante = {
                    "id": cursox['estudiantes.id'],
                    "nombre": cursox['estudiantes.nombre'],
                    "apellido": cursox['apellido'],
                    "edad": cursox['edad'],
                    "created_at": cursox['created_at'],
                    "updated_at": cursox['updated_at'],
                }
            curso.estudiantes.append(Estudiante(datos_estudiante))
        return curso
