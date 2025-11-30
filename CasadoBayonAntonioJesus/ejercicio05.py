#Escriba un programa que pida dos números (m y n) y que escriba n segmentos de m estrellas
#separados por m espacios, como muestran los ejemplos siguientes:


def solicitar_numeros():
   
    m = int(input("Escriba el número de estrellas por segmento (m): "))
    n = int(input("Escriba el número de segmentos (n): "))
    return m, n


def dibujar_segmentos(m, n):
   
    resultado = ""
    for i in range(n):
        
        resultado += "* " * m
       
        if i < n - 1:
            resultado += "  " * m
    print(resultado)


def main():
    
    m, n = solicitar_numeros()
    dibujar_segmentos(m, n)


main()

