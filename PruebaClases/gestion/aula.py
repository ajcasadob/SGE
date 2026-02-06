from modelo.alumno import Alumno
from modelo.profesor import Profesor


class Aula:
    def __init__(self,nombre:str,tutor:Profesor):
        self.nombre = nombre
        self.tutor= tutor
        self.alumnos: list[Alumno]=[]
    
    def __str__(self):
        return f"(nombre: {self.nombre}, tutor {self.tutor}, alumnos: {self.alumnos})"
        
        
    def agregar_alumno(self, alumno:Alumno):
        self.alumnos.append(alumno)
        
        
    def calcular_nota_media(self):
        if not self.alumnos:
            return 0.0
        
        suma_notas = sum(alumno.nota for alumno in self.alumnos)
        return suma_notas/len(self.alumnos)