#Escriba un programa que pida tres números enteros distintos y que escriba una lista que empiece por
#el más pequeño y termine en el más grande.


#Escriba un programa que pida tres números enteros distintos y que escriba una lista que empiece por
#el más pequeño y termine en el más grande.

def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

def mostrar_resultado(lista_ordenada):
    print(f"Lista ordenada: {lista_ordenada}")

def main():
    
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    num3 = int(input("Introduce el tercer número entero: "))
    
    lista_ordenada = ordenar_numeros(num1, num2, num3)
    mostrar_resultado(lista_ordenada)

main()