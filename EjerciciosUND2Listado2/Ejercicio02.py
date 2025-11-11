productos = ('pan','leche','huevos','queso')


repetir = True

while repetir:
    
    el= int(input('''
        0. Salir
        1. Mostrar el primer y ultimo elemeto
        2.Contar cuantas veces aparece un producto(elige uno)
        3. Convertir una lista, modificar un elemento y volver a tupla
        4. Añadir un nuevo producto( tupla concatenada)'''))
    match el:
        case 0:
            repetir = False
            print('Saliendo..')
        case 1:
            
            primerElemento = productos[0]
            print(f'El primer elemento es {primerElemento}')
            ultimoElemento = productos[3]
            print(f'El ultimo elemento es {ultimoElemento}')
        case 2:
            
            print(productos.count('huevos'))
        case 3:
            
            lista = list(productos)
            lista[0]= 'Jamon'
            tuple(lista)
            print(lista)
        case 4:
            productoDos = ('Azucar','Cruzcampo')
            nuevaList= productos + productoDos
            print(nuevaList)
        case _:
            print('La eleccion elegida no esta establecida')    
                