notas = []


nNotas =int(input('Introduce el numero de notas'))
for i in range  (nNotas):
    notas = float(input(f'Dime la {i+1} nota'))

if notas >= 0 and notas <= 10:
        resultado = len(notas)

        print(f'La media de notas es {resultado}')