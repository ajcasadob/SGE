inventario = {'manzanas':10, 'naranjas':5,'peras':8}

repetir = True
sumaTotal = 0.0


while repetir:
    
    el= int(input('''
            0. Salir
            1. Mostar todas las claves y valores
            2. Aumentar manzanas en 5
            3.Eliminar peras
            4. Calcular el total de frutas'''))
    match el:
        case 0:
            repetir =False
            print('Gracias por elegir mi programa')
        case 1:
            for i, j in inventario.items():
                print(f'Productos {i} y cantidades {j}')
        case 2:
            
            inventario['manzanas']+=5
            for i, j in inventario.items():
                print(f'Productos {i} y cantidades {j}') 
                
        case 3:
                    del inventario['peras']
        case 4:
                    for i, j in inventario.items():
                        sumaTotal+=j  
                    
                    print(f'El total de inventario es de {sumaTotal}')  
        case _:
            print('La opcion elegida no esta establecida')                     
