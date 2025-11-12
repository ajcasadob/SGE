import random

repetir = True
alumnos = {
    "12345678A": random.randint(1, 10),
    "87654321B": random.randint(1, 10),
    "23456789C": random.randint(1, 10),
    "98765432D": random.randint(1, 10),
    "34567890E": random.randint(1, 10)
}

while repetir:
    
    el = int(input('''
                0. Salir
                1. Mostrar los datos
                2. Añadir un nuevo estudiante
                3. Crear un nuevo diccionario, solo con los estudiantes que tienen nota media mayor a una valor dado por teclado
                4. Modificar un estudiante
                '''))
    match el:
        
        case 0:
            repetir= False
            print('Gracias por elegir mi programa')
        case 1:
            for i, j in alumnos.items():
                print(f'DNI {i} - Nota {j}')   
            
        case 2:
            
            dni=str(input('Introduce el dni del alumno'))
            nota = float(input('Introduce la nota del alumno'))
            
            alumnos[dni]=nota
            
            for i, j in alumnos.items():
                print(f'DNI {i} - Nota {j}') 
        case 3:
            newNotaMedia = {}
            nota =float(input('Dime la nota que quieres comprobar'))
            
            for dni,notaV in alumnos.items():
                if notaV >= nota:
                    newNotaMedia[dni]=notaV
            
            print(f'Los alumnos con DNI que pasan el corte {newNotaMedia}')        
                
            
        case 4:
            
            dni=str(input('Dime el dni del alumno que quieres modificar la nota'))  
            
            if dni in alumnos:
                print(f'Nota actual:{alumnos[dni]}')
                newNota=float(input('Introduce la nota nueva'))
                alumnos[dni]=newNota
                print(f'Nota actulizada correctamente a {newNota}')
            else:
                print('Alumno no encontrado')    
               
                    
    
