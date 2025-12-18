#Crea una función estado_bateria(porcentaje) que:

#- Devuelva "Perfecto" si porcentaje está entre 80 y 100.
#- Devuelva "Aceptable" entre 30 y 79.
#- Devuelva "Modo ahorro YA" entre 10 y 29.
#- Devuelva "Busca un enchufe" si es menor que 10.

def estado_bateria(porcentaje):
    
    if porcentaje>80 and porcentaje<100:
        print('Perfecto')
    elif porcentaje > 30 and porcentaje <79:
        print('Aceptable')  
    elif porcentaje>10 and porcentaje < 29:
        print('Modo ahorro YA')    
    else:
        print('Busca un enchufe')
        
        

    

estado_bateria(81)
estado_bateria(40)
estado_bateria(15)
estado_bateria(3)    


