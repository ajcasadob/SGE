#Escriba un programa que pida tres números enteros distintos y que escriba una lista que empiece por
#el más pequeño y termine en el más grande.


def solicitar_numeros():
    
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    num3 = int(input("Introduce el tercer número entero: "))
    return num1, num2, num3


def ordenar_numeros(num1, num2, num3):
    
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

def ordenar_manual(numeros):
    newList= []
    for i in numeros:
        maxNum = max(numeros)
        mixNum = min(numeros)
        newList.insert(0,mixNum)
        newList.insert(2, maxNum)
   
    
    
    return numeros
    

def mostrar_resultado(lista_ordenada):
    
    print(f"Lista ordenada: {lista_ordenada}")
    


def main():
    
    numero1, numero2, numero3 = solicitar_numeros()
    lista_ordenada = ordenar_numeros(numero1, numero2, numero3)
    mostrar_resultado(lista_ordenada)
   


main()
