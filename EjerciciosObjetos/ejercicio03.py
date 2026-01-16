from datetime import datetime

inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def buscar_inmuebles(inmuebles, presupuesto):
    
    año_actual = datetime.now().year
    resultado = []
    
    for inmueble in inmuebles:
        # Crear una copia del inmueble para no modificar el original
        inmueble_copia = inmueble.copy()
        
        # Calcular antigüedad
        antiguedad = año_actual - inmueble['año']
        
        # Calcular precio base
        precio_base = (inmueble['metros'] * 1000 + 
                      inmueble['habitaciones'] * 5000 + 
                      inmueble['garaje'] * 15000)
        
        # Aplicar depreciación por antigüedad
        precio_con_antiguedad = precio_base * (1 - antiguedad / 100)
        
        # Aplicar factor de zona
        if inmueble['zona'] == 'A':
            precio_final = precio_con_antiguedad
        elif inmueble['zona'] == 'B':
            precio_final = precio_con_antiguedad * 1.5
        else:
            precio_final = precio_con_antiguedad
        
        # Agregar precio al inmueble
        inmueble_copia['precio'] = precio_final
        
        # Añadir a la lista si está dentro del presupuesto
        if precio_final <= presupuesto:
            resultado.append(inmueble_copia)
    
    return resultado


# Ejemplo de uso
presupuesto_maximo = 100000
resultado = buscar_inmuebles(inmuebles, presupuesto_maximo)

print(f"Inmuebles con presupuesto máximo de {presupuesto_maximo}€:")
print("-" * 60)
for inmueble in resultado:
    print(f"Año: {inmueble['año']}, Metros: {inmueble['metros']}, "
          f"Habitaciones: {inmueble['habitaciones']}, Garaje: {inmueble['garaje']}, "
          f"Zona: {inmueble['zona']}, Precio: {inmueble['precio']:.2f}€")
print(f"\nTotal de inmuebles encontrados: {len(resultado)}")