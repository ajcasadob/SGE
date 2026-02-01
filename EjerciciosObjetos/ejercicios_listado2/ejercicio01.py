def aplicar_descuento(precio, porcentaje):
    return precio * (1 - porcentaje / 100)


def aplicar_iva(precio, porcentaje):
    return precio * (1 + porcentaje / 100)


def calcular_precio_cesta(cesta, funcion):
    precio_total = 0
    for producto, (precio, porcentaje) in cesta.items():
        precio_total += funcion(precio, porcentaje)
    return precio_total



cesta = {}

num_productos = int(input("¿Cuántos productos? "))

for i in range(num_productos):
    nombre = input(f"Producto {i+1}: ")
    precio = float(input("Precio: "))
    porcentaje = float(input("Porcentaje: "))
    cesta[nombre] = (precio, porcentaje)

opcion = input("\n¿Aplicar (1) Descuento o (2) IVA? ")

if opcion == "1":
    total = calcular_precio_cesta(cesta, aplicar_descuento)
    print(f"\nTotal con descuentos: {total:.2f}€")
else:
    total = calcular_precio_cesta(cesta, aplicar_iva)
    print(f"\nTotal con IVA: {total:.2f}€")
