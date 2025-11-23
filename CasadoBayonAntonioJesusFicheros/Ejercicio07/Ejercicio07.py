# Crea un programa que lea los datos de clientes y los vaya escribiendo en un fichero de texto

archivo = open('clientes.txt', 'w')

while True:
    print("\n--- Registro de Cliente ---")
    nombre = input("Nombre (o 'salir' para terminar): ")
    
    if nombre.lower() == 'salir':
        break
    
    apellido1 = input("Apellido1: ")
    apellido2 = input("Apellido2: ")
    edad = input("Edad: ")
    
    archivo.write(f"Nombre:\t\t\t{nombre}\n")
    archivo.write(f"Apellido1:\t\t{apellido1}\n")
    archivo.write(f"Apellido2:\t\t{apellido2}\n")
    archivo.write(f"Edad:\t\t\t{edad}\n")
    archivo.write("\n")
    
    print("Cliente registrado correctamente.")

archivo.close()
print("Archivo 'clientes.txt' creado exitosamente.")
