#Crea una función maraton_series(horas) que reciba un número de horas vistas de series y devuelva
#una tupla con (dias, horas_restantes).
#Ejemplo: 27 horas → (1, 3).


def maraton_series(horas):
    
    dias = horas // 24  
    horas_restantes = horas % 24  
    return (dias, horas_restantes)

print(maraton_series(27))
