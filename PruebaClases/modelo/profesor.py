class Profesor:
    def __init__(self, nombre:str, asignatura:str):
        self.nombre= nombre
        self.asignatura = asignatura
    
    def __str__(self):
        return f"Profesor(nombre={self.nombre}, asignatura = {self.asignatura})"