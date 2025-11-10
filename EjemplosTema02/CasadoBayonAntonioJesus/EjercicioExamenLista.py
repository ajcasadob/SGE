#Voy a alquilar una habitación de mi casa a modo de apartamento turístico y necesito un programa para gestionar lo
#recaudado. Se debe usar una lista como estructura principal para guardar los datos (si hace falta alguna tupla se puede
#usar). Como no hemos dado todavía objetos, lo haremos con una lista de flotantes, que será lo recaudado cada día que lo
#alquilo.

#El programa puede empezar creando una lista directamente con datos y luego poder hacer lo siguiente mediante un menú
#en la clase Principal y debe mostrar en la misma

#Agregar una nueva recaudación.
#• Poner a cero una recaudación (se me ha ido el cliente sin pagar).
#• Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito.
#• Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad.
#• Sumar una cantidad a un día como gasto extra.
#• Calcular cuánto he recaudado en todas las recaudaciones.
#• Ordenar la lista de mayor a menor.
#• Calcular la media diaria.
#• Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada.
#• Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes.


recaudacion = [50,55,60,44,60,100,150]


repetir = True
contador =0
total=0
media = 0

while repetir:
    
    el= int(input('''
    0. Salir
    1. Agregar una nueva recaudación
    2.Poner a 0 una recaudacion
    3.Imprimir toda la lista
    4.Buscar el dia que mas he ganado
    5.Sumar una cantidad
    6.Calcular cuanto he recaudado
    7.Ordenar la lista de mayor a menor
    8. Calcula la media diaria
    9.Calcular porcentaje de dias al mes en las que he tenido la habitacion alguilada
    10. Dividir la lista en dos nuevas listas
                    '''))
    
    match el:
        case 0:
            print('Saliendo..')
            repetir = False
        case 1:
            dia =float( input('¿Cuantos quieres agregar?'))
            recaudacion.append(dia)
        case 2:
        
            indice = int(input('¿Que dia quieres poner a 0 la recaudación?'))
            
            recaudacion[indice-1]=0
        case 3:
            
                print(recaudacion)
        case 4:
            for i in recaudacion:
                if i == max(recaudacion):
                    contador +=1
                    print(i)
                    
            print(f'Ha habido {contador} dias que has ganado mas')
        case 5:
                    dia= int(input('¿Que dia quiere sumar la cantidad?'))
                    extra = float(input('¿Que gasto extra quieres sumar?'))
                    recaudacion[dia-1] +=extra
        case 6:
                        
                total= sum(recaudacion)
                print(f'Has recaudado un total de  {recaudacion} € ')
        case 7:
                print(sorted(recaudacion))
        case 8:
                media = sum(recaudacion)/len(recaudacion)
                print(f'La media diaria es de {media} €')
        case 9:
                dias_ocupados = sum(1 for x in recaudacion if x >0)
                porcentaje = dias_ocupados / 30*100
                print(f'Porcentaje de ocupacion sobre los 7 dias: {porcentaje:.2f} % ({dias_ocupados}/ 7 días)')
        case 10 :
                print
        case _:
            print('Opción incorrecta, intentolo de nuevo..')        