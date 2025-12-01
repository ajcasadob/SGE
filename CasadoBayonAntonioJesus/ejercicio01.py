#Escriba un programa que pida un número. Después pregunte cuántos números se van a introducir, pida
#esos números, y escriba cuántos de esos números era mayor que el anterior.

num = int(input('Introduce un numero'))

listaNumeros = [num]

numLista = int(input('Cuantos numeros desea introducir'))



for i in range (numLista):
    
    numIntroducir= int(input('Introduce esos numeros'))
    listaNumeros.append(numIntroducir)

def lista():
    mayores =[]
    for i in range(1, len(listaNumeros)):
        if listaNumeros[i] > listaNumeros[i-1]:
            mayores.append(listaNumeros[i])
    
    print(f'Los numeros mayores que el anterior son : {mayores}') 
    print(f'La cantidad de numeros mayores es {len(mayores)}')

    

    
lista()     
    