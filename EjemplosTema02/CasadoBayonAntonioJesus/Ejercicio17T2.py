import random


temperatura = [
    ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'],
    []
]

desde = int(input('Desde que numero rellenar'))
hasta = int(input('Hasta que numero quieres rellenar'))


for i in range (len(temperatura[0])):
    temperatura[1].append(random.randint(desde,hasta))

for dias,grados in zip (temperatura[0],temperatura[1]):
    print(dias,grados)

media = round(sum(temperatura[1])/len(temperatura[1]),2)




for i in range(len(temperatura[1])):
    if temperatura[1][i] == max(temperatura[1]):
        dia_max = temperatura[0][i]
    if temperatura[1][i] == min(temperatura[1]):
        dia_min = temperatura[0][i]
print(f'La temperatura máxima fue de {max(temperatura[1])} grados el día {dia_max}')
print(f'La temperatura mínima fue de {min(temperatura[1])} grados el dia {dia_min}')



temperatura_ordenada = sorted(temperatura[1])
print('Las temperaturas ordenadas de mayor a menor son:')
for temp in temperatura_ordenada:
    print(temp)

superiorMedia = []
for i in range (len(temperatura[1])):
    if temperatura[1][i]>media:
        superiorMedia.append(temperatura[1][i])
        print(f'El día {temperatura[0][i]}tuvo una temperatura por encima de la media de la semana ')


for i in range(len(superiorMedia)):
    print(f'Las temperaturas por encima de la media son: {superiorMedia[i]}')
    

print(media)

