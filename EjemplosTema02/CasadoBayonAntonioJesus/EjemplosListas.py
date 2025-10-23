bebidas = ['Agua', 'Pepsi', 'Alcohol', 'Sidra', 'Cerveza']

opcion = -1

while opcion != 0:

    print("\n======== MENÚ DE OPERACIONES CON LISTAS ========")
    print("1. Invertir una lista (reverse)")
    print("2. Añadir un elemento al final (append)")
    print("3. Insertar en cualquier posición (insert)")
    print("4. Repetir lista (operador *)")
    print("5. Unir listas sin modificar la original (+)")
    print("6. Unir listas modificando la original (extend)")
    print("7. Modificar un elemento por su índice")
    print("8. Borrar por índice (del)")
    print("9. Borrar por valor (remove)")
    print("10. Vaciar la lista por completo (clear)")
    print("11. Buscar el índice de un valor (index)")
    print("12. Comprobar si un valor está en la lista (in)")
    print("13. Contar apariciones de un valor (count)")
    print("14. Convertir lista en texto (join)")
    print("15. Ordenar lista con sorted()")
    print("16. Número de elementos de la lista (len)")
    print("17. Iterar elementos con for")
    print("18. Iterar con enumerate")
    print("19. Iterar dos listas con zip")
    print("0. Salir")
    print("================================================")

    opcion = int(input("Selecciona una opción: "))

    match opcion:
        case 1:
            print("Invertir una lista usamos la función reverse()")
            bebidas.reverse()
            print(bebidas)

        case 2:
            print("Utilizamos append() para añadir al final de la lista")
            nuevo = input("Introduce un nuevo producto: ")
            bebidas.append(nuevo)
            print(bebidas)

        case 3:
            print("Utilizamos insert() para añadir en cualquier posición")
            nuevo = input("Producto a insertar: ")
            pos = int(input("Posición (0-n): "))
            bebidas.insert(pos, nuevo)
            print(bebidas)

        case 4:
            print("El operador * nos permite repetir los elementos de una lista")
            rep = int(input("¿Cuántas veces repetir la lista?: "))
            print(bebidas * rep)

        case 5:
            print("Unimos listas con + sin modificar la original")
            comida = ['Filetes', 'Huevos', 'Arroz', 'Merluza', 'Ternera']
            print(bebidas + comida)

        case 6:
            print("extend() modifica la lista original añadiendo otra")
            comida = ['Filetes', 'Huevos', 'Arroz', 'Merluza', 'Ternera']
            bebidas.extend(comida)
            print(bebidas)

        case 7:
            print("Para modificar accedemos al índice del elemento")
            indice = int(input("Índice a modificar: "))
            nuevo = input("Nuevo valor: ")
            bebidas[indice] = nuevo
            print(bebidas)

        case 8:
            print("Borrar por índice usando del")
            indice = int(input("Índice a borrar: "))
            del bebidas[indice]
            print(bebidas)

        case 9:
            print("Borrar por valor usando remove()")
            valor = input("Valor a borrar: ")
            if valor in bebidas:
                bebidas.remove(valor)
                print(bebidas)
            else:
                print("Ese valor no está en la lista")

        case 10:
            print("Utilizando clear() vaciamos la lista completa")
            bebidas.clear()
            print(bebidas)

        case 11:
            print("index() nos devuelve el índice de un valor")
            valor = input("Valor a buscar: ")
            if valor in bebidas:
                print(bebidas.index(valor))
            else:
                print("Ese valor no está en la lista")

        case 12:
            print("in nos permite comprobar si un valor existe en la lista")
            valor = input("Valor a comprobar: ")
            print(valor in bebidas)

        case 13:
            print("count() cuenta cuántas veces aparece un valor")
            valor = input("Valor a contar: ")
            print(bebidas.count(valor))

        case 14:
            print("join() convierte la lista en una cadena de texto")
            sep = input("Separador (ej: , o -): ")
            print(sep.join(bebidas))

        case 15:
            print("sorted() ordena la lista sin modificar la original")
            print(sorted(bebidas))

        case 16:
            print("len() devuelve el número de elementos")
            print(len(bebidas))

        case 17:
            print("Iterar elementos con un for")
            for elem in bebidas:
                print(elem)

        case 18:
            print("Iterar con enumerate para obtener índice y valor")
            for i, elem in enumerate(bebidas):
                print(i, elem)

        case 19:
            print("zip() permite iterar dos listas a la vez")
            tiendas = ['Amazon', 'PcComponentes', 'PcBox']
            componentes = ['Intel', 'AMD', 'Nvidia']
            for t, c in zip(tiendas, componentes):
                print(t, c)

        case 0:
            print("👋 Saliendo del programa...")

        case _:
            print("❌ Opción no válida")