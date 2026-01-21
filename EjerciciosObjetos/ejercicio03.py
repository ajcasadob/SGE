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
       
        inmueble_copia = inmueble.copy()
        
        antiguedad = año_actual - inmueble['año']
        
       
        precio_base = (inmueble['metros'] * 1000 + 
                      inmueble['habitaciones'] * 5000 + 
                      inmueble['garaje'] * 15000)
        
       
        precio_con_antiguedad = precio_base * (1 - antiguedad / 100)
        
        
        if inmueble['zona'] == 'A':
            precio_final = precio_con_antiguedad
        elif inmueble['zona'] == 'B':
            precio_final = precio_con_antiguedad * 1.5
        else:
            precio_final = precio_con_antiguedad
        
       
        inmueble_copia['precio'] = precio_final
        
      
        if precio_final <= presupuesto:
            resultado.append(inmueble_copia)
    
    return resultado


presupuesto_maximo = 100000
resultado = buscar_inmuebles(inmuebles, presupuesto_maximo)

print(f"Inmuebles con presupuesto máximo de {presupuesto_maximo}€:")
print("-" * 60)
for inmueble in resultado:
    print(f"Año: {inmueble['año']}, Metros: {inmueble['metros']}, "
        f"Habitaciones: {inmueble['habitaciones']}, Garaje: {inmueble['garaje']}, "
        f"Zona: {inmueble['zona']}, Precio: {inmueble['precio']:.2f}€")
print(f"\nTotal de inmuebles encontrados: {len(resultado)}")