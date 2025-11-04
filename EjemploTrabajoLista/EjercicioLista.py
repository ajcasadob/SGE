#Un estudiante del colegio San Pedro quiere analizar por que suspende siempre programación,
# por ello se le ha ocurrido hacer un programa para ver cuánto tiempo dedica a 
# jugar videojuegos durante una semana. Vamos a crear una lista para anotar 
# las horas que juega cada dia, la llamaremos (horas_juego) y cada elemento representa un dia.

#1.Muestra por pantalla:
#*El total de horas jugadas en la semana.
#*El promedio de horas diarias.
#*El día en el que más jugó y el día en el que menos jugó.

#2.Crea una nueva lista que contenga solo los días en los que jugó más de 2 horas.
#3.Añade al final de la lista las horas jugadas un domingo extra (por ejemplo, en una nueva semana) y vuelve a mostrar la lista actualizada.
#4. Por ultimo muestra la lista con los dias que jugo mas de 3 horas.          


dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
horas_juego = []
total = 0.0
promedio = 0.0
max_horas = 0.0
min_horas = 0.0
dia_max = ""
dia_min = ""
dias_mas_3 = 0
domingo_extra = 0.0

for dia in dias_semana:
    horas = float(input(f"Introduce las horas jugadas el {dia}: "))
    horas_juego.append(horas)

print("\nHoras jugadas por día:", horas_juego)

total = sum(horas_juego)
promedio = total / len(horas_juego)

print("Total de horas:", total)
print("Promedio diario:", round(promedio, 2))

max_horas = max(horas_juego)
min_horas = min(horas_juego)
dia_max = dias_semana[horas_juego.index(max_horas)]
dia_min = dias_semana[horas_juego.index(min_horas)]

print(f"Día con más horas: {dia_max} ({max_horas} horas)")
print(f"Día con menos horas: {dia_min} ({min_horas} horas)")

print("\nDías con más de 2 horas de juego:")
for i in range(len(horas_juego)):
    if horas_juego[i] > 2:
        print(f"{dias_semana[i]}: {horas_juego[i]} horas")

domingo_extra = float(input("\nIntroduce las horas jugadas en un domingo extra: "))
horas_juego.append(domingo_extra)
print("Lista actualizada:", horas_juego)

for horas in horas_juego:
    if horas > 3:
        dias_mas_3 += 1

print(f"Días con más de 3 horas de juego: {dias_mas_3}")


