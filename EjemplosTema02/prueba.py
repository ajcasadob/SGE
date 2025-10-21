# Requiere Python 3.10+
# Primera lista ya introducida manualmente (no pide por teclado)
lista = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

running = True
while running:
    print("""
Menú:
1  - reverse
2  - append
3  - insert (posición)
4  - repetir (*)
5  - concatenar (+)
6  - extend
7  - modificar por índice
8  - borrar por índice (del)
9  - borrar por valor (remove)
10 - borrar por rango (start,end)
11 - clear
12 - reinicializar a []
13 - index
14 - in
15 - count
16 - join
17 - sorted (no modifica)
18 - sort (in-place)
19 - len
20 - iterar for
21 - iterar enumerate
22 - zip con otra lista
23 - ver lista actual
0  - salir
""")
    opcion = input("Elige opción: ")

    match opcion:
        case "1":
            lista.reverse()
            print(lista)
        case "2":
            lista.append(input("Elemento a añadir: "))
            print(lista)
        case "3":
            pos = int(input("Posición (0-based): "))
            lista.insert(pos, input("Elemento: "))
            print(lista)
        case "4":
            times = int(input("Repeticiones (>=0): "))
            print(lista * times)
        case "5":
            otra = [s for s in input("Otra lista (coma-separada): ").split(",") if s]
            print(lista + otra)
        case "6":
            otra = [s for s in input("Otra lista para extend: ").split(",") if s]
            lista.extend(otra)
            print(lista)
        case "7":
            pos = int(input("Índice a modificar: "))
            lista[pos] = input("Nuevo valor: ")
            print(lista)
        case "8":
            pos = int(input("Índice a borrar: "))
            del lista[pos]
            print(lista)
        case "9":
            lista.remove(input("Valor a eliminar: "))
            print(lista)
        case "10":
            start = int(input("Start: "))
            end = int(input("End (exclusive): "))
            del lista[start:end]
            print(lista)
        case "11":
            lista.clear()
            print(lista)
        case "12":
            lista = []
            print(lista)
        case "13":
            print("Índice:", lista.index(input("Valor a buscar: ")))
        case "14":
            val = input("Valor a comprobar: ")
            print(val in lista)
        case "15":
            print("Count:", lista.count(input("Valor a contar: ")))
        case "16":
            sep = input("Separador para join: ")
            print(sep.join(lista))
        case "17":
            print("Sorted (nuevo):", sorted(lista))
        case "18":
            lista.sort()
            print(lista)
        case "19":
            print("Len:", len(lista))
        case "20":
            for e in lista:
                print(e)
        case "21":
            for i, e in enumerate(lista):
                print(i, e)
        case "22":
            otra = [s for s in input("Otra lista para zip: ").split(",") if s]
            for a, b in zip(lista, otra):
                print(a, b)
        case "23":
            print("Lista actual:", lista)
        case "0":
            running = False
            print("Saliendo...")
        case _:
            print("Opción no válida.")