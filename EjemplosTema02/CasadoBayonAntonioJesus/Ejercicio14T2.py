#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo


palabra=str(input('Introduce una palabra'))



if palabra == palabra[::-1]:
    print('Es palindromo')
else:
    print('no es palindromo')
   