from gestion.aula import Aula
from modelo.alumno import Alumno
from modelo.profesor import Profesor



    
    
def main():
        
        profesor = Profesor("Ana","Matematicas")
        
        aula = Aula("1ºBachillerato A", profesor)
        
        alumno1= Alumno("Luis",4.5)
        alumno2= Alumno("Pepe",5.5)
        
        aula.agregar_alumno(alumno1)
        aula.agregar_alumno(alumno2)
        
        print(aula)
        print(f"Nota media del alumnno{aula.calcular_nota_media}")
        
        



if __name__== "__main__":
    main()