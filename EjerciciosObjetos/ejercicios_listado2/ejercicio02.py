import math

def calculadora_cientifica():
    valor = int(input("Introduce el valor: "))
    
    print("\n1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Exponencial")
    print("5. Logaritmo neperiano")
    
    opcion = int(input("\nElige opción (1-5): "))
    
    print("\nNúmero\tResultado")
    print("-" * 25)
    
    for i in range(1, valor + 1):
        match opcion:
            case 1:
                resultado = math.sin(i)
            case 2:
                resultado = math.cos(i)
            case 3:
                resultado = math.tan(i)
            case 4:
                resultado = math.exp(i)
            case 5:
                resultado = math.log(i)
            case _:
                print("Opción no válida")
                return
        
        print(f"{i}\t{resultado:.6f}")

calculadora_cientifica()
