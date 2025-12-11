def es_bisiesto(año):
    return (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)

año = int(input("Introduce un año: "))
print(es_bisiesto(año))
