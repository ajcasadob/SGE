repetir = True

print ("Bienvenidos a mi programa, vamos a calcular diferentes nominas")
print("A continuación te muestro las diferents opciones de menu")



while repetir:

    elegir = int(input("""
    0 . Salir
    1. Calcular sueldo
"""))
    match elegir:
        case 0:
            print("Gracias por elegir este programa")
            repetir= False
        case 1:

            nombre = input("Diga usted su nombre\n")   
            horasTrabajo= float(input("Indique cuanto cobra la hora de trabajo\n"))
            diasSemana = int(input("Cuantos dias trabajas a la semana\n"))
            HorasExtraCobro= float(input("Cuanto cobra la hora extra\n"))
            HorasExtras = float(input("Cuantas horas extras tienes\n"))


            resultado = horasTrabajo * diasSemana + (HorasExtraCobro*HorasExtras)

            print(f"Usted cobra al mes {resultado} €")


        case _:
            print("Esa opción no esta establecida")