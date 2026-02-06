class Alumno:
    def __init__(self, nombre:str, nota:float):
        self.nombre = nombre
        self.nota = nota
        
    
    def __str__(self):
        return f"(Alumno{self.nombre}, Nota{self.nota})"