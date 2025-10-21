
#Tienes una lista de la compra inicial llamada lista = ['Agua', 'Huevos', 'Aceite'].
#  Escribe un programa que pida al usuario que introduzca 3 productos, uno a uno. 
# Cada producto debe añadirse al final de la lista usando el método append.
#  Al terminar, muestra la lista completa con los productos nuevos añadidos al final.





lista = ['Agua', 'Huevos', 'Aceite']

while True:
    print("\n Lista de la compra actual:", lista)
    print("Vas a añadir 3 productos nuevos.\n")

    
    for i in range(3):
        producto = ""
        
        
        while producto == "":
            producto = input("Introduce el producto " + str(i + 1) + ": ")
            if producto == "":
                print("No puedes dejar el nombre vacío, inténtalo de nuevo.")
        
        
        lista.append(producto)

    
    print("\n✅ Lista final de la compra con los nuevos productos:")
    for elemento in lista:
        print("-", elemento)

  
    print("\nPulsa 0 para salir o cualquier otro número para continuar.")
    opcion = int(input("Opción: "))

    if opcion == 0:
        print("\n Programa finalizado. ¡Hasta la próxima!")
        break