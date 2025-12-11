
def buggy (arg, result=[]):
    result.append(arg)
    print(result)
    
buggy('a',[])
buggy('b',[])
buggy( 'a' , [ 'x' , 'y', 'z' ])

buggy( 'b' , [ 'x ', 'y' , 'z' ])


def works(arg):
    result = []
    result.append(arg)
    return result

works('a')
works('b')


# EJERCICIO: DICCIONARIO DE CRITERIOS Y NOTAS

def ingresarNotas():
   
    notasCriterios = {}
    
    num = int(input('¿Cuántos criterios de evaluación hay? '))
    
    for i in range(num):
        criterio = input(f'Nombre del criterio {i+1}: ')
        nota = float(input(f'Nota del criterio "{criterio}": '))
        notasCriterios[criterio] = nota
    
    return notasCriterios


def calcularNotaMedia(diccionario):
    
    if len(diccionario) == 0:
        return 0
    
    suma = sum(diccionario.values())
    media = suma / len(diccionario)
    return media


def mostrarNotas(diccionario):
   
    print("\n--- NOTAS POR CRITERIO ---")
    for criterio, nota in diccionario.items():
        print(f"{criterio}: {nota}")
    print("-" * 30)


def mostrarEstadisticas(diccionario):
    """
    Muestra estadísticas completas: media, máxima, mínima
    """
    if len(diccionario) == 0:
        print("No hay notas registradas")
        return
    
    media = calcularNotaMedia(diccionario)
    maxNota = max(diccionario.values())
    minNota = min(diccionario.values())
    
    criterioMax = [crit for crit, nota in diccionario.items() if nota == maxNota]
    criterioMin = [crit for crit, nota in diccionario.items() if nota == minNota]
    
    print(f"\nNota media: {media:.2f}")
    print(f"Nota máxima: {maxNota} - Criterio(s): {', '.join(criterioMax)}")
    print(f"Nota mínima: {minNota} - Criterio(s): {', '.join(criterioMin)}")


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("=== GESTIÓN DE CRITERIOS Y NOTAS ===\n")
    
    # Ingresar notas
    misNotas = ingresarNotas()
    
    # Mostrar todas las notas
    mostrarNotas(misNotas)
    
    # Mostrar estadísticas
    mostrarEstadisticas(misNotas)
    
    