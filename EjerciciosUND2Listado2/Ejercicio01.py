temperaturas = (21,24,19,30,25,28)
media = 0.0 
repetir = True



while repetir:
    el = int(input('''
                0. Salir
                1. Mostrar el valor maximo y minimo
                2. Calcular temperatura media
                3. Convertir una tupla en lista, añadir una nueva temperatura y volver a convertir en tupla
                4. Comprobar si 30 esta presente'''))
    
    match el:
        
        case 0:
            print('Saliendooo')
            repetir = False
        case 1:
            print(max(temperaturas))
            print(min(temperaturas))
        case 2:
            
            for i in temperaturas:
                media=sum(temperaturas)/(len(temperaturas) )
            
            print(media)
        case 3:
            lista = list(temperaturas)
            lista.append(40)
            tuple(lista)
            print(lista)
        case 4:
            
                if 30 in temperaturas:
                    print('Esta presente')
                else:
                    print('No esta presente')   
        case _:
            print('La opcion elegida no esta establecida')                 