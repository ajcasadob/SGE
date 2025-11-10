#Estoy dando clases de inglés para el B2 y me gustaría que me ayudarais a crear un diccionario para ver cómo
#se dicen palabras con significado “raro” españolas en inglés. Se hará todo en el mismo archivo, no se crean
#clases. Por ejemplo, “Cabeza: (en el sur de España) amigo/colega”, aro: sí, de acuerdo. Consideraremos que
#no se repiten palabras con el mismo nombre, es decir, que la palabra “take” no aparece dos veces en el
#diccionario y que, si tiene varios significados, estos pueden ir en el mismo String “significado”, por ejemplo,
#for---->por, para, durante.

#Se debe utilizar un diccionario que se puede instanciar con algunos elementos de inicio y un menú para cada
#uno de las siguientes funcionalidades:

#Agregar una nueva palabra por teclado.
#Imprimir el diccionario completo “en bonito”.
#Buscar una palabra por nombre y mostrar su significado evitando que salta un error si la palabra no se
#encuentra.
#• Modificar una palabra, modificando únicamente el significado de esta por otro nuevo, leído por
#teclado.
#• Pedir al usuario sus dos palabras favoritas con los significados y combinar este con el ya creado
#modificando el original.
#• Borrar una palabra (ustedes decidís la mejor forma).
#• Ordenar el diccionario por orden alfabético.

diccionario = {'aro': 'Si',
            'cabeza': 'colega',
            'no ni na': 'correcto'}

repetir = True


while repetir:

        el = int(input('''
            0.Salir
            1.Agregar una nueva palabra
            2.Imprimir el diccionario completo 
            3.Buscar una palabra por nombre y mostrar sus significado evitando que salta un error si la palabra no se encuentra\n'''))
        match el:
            case 0:
                print('Saliendo..')
                repetir = False
            case 1:
                clave = input('Que palabra quieres añadir')
                valor = input ('Que valor quieres añadir')
                diccionario[clave] = valor
                
            case 2:
                    
                    for word, meaning in diccionario.items():
                        print(f'{word}: {meaning}')
            case 3:
                    palabraBuscar = input('Que significado quieres buscar')
                    print(diccionario.get(palabraBuscar))
            case 4:

                    palabraBuscar = input('Que palabra quieres buscar')
                    significadoModificar = input('Que quieres añadir')
                    diccionario[palabraBuscar]=significadoModificar
                    
                    
            case 5:
                print
            case 6:
                
                palabraEliminar = input('Que palabra quieres eliminar')
                del diccionario [palabraEliminar]   
            case 7:
                    
                    print(sorted(diccionario.items()))
                        
                    
                    
            case _:
                print('La opcion elegida no esta establecida')       