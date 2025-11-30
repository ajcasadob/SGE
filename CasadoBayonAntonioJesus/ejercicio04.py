#Escriba un programa que pida un número y dibuje dos cuadrados de ese número de estrellas en
#diagonal, como muestran los ejemplos siguientes:


def solicitar_numero():
    
    numero = int(input("Escriba un número entero positivo: "))
    return numero


def dibujar_cuadrados(n):
    
    
    for i in range(n):
        
        espacios = " " * (i * 2)
        
        estrellas = "* " * n
        print(espacios + estrellas)
    

    for i in range(n):
        
        espacios = " " * ((n + i) * 2)
        
        estrellas = "* " * n
        print(espacios + estrellas)


def main():
    
    numero = solicitar_numero()
    dibujar_cuadrados(numero)


main()

