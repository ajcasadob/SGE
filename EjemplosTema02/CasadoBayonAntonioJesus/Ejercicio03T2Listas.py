notas = []
media =0.0

nNotas =int(input('Introduce el numero de notas'))
for i in range  (nNotas):
    notas = float(input(f'Dime la {i+1} nota'))

if notas >10 and notas < 0:
        print('Introduce una nota válida')
else:
        notas.append(notas)

print(f'Tus notas son las siguientes{notas}')

for i in notas:
    media+=i        

media= media/len(notas)
print(f'La media de todas las notas es {media}')
print(f'La nota mas alta es {max(notas)} y la nota mas baja es {min(notas)}')    