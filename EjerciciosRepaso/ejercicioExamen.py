maxHorasExtras = 30
dineroExtraHora1 = 40.0
dineroExtraHora2 = 50.0
dineroExtraHora3 = 75.0
porcentajeAnt = 2.0
porcentajeEdad = 4.0
salarioBase = 1300.0
repetir = True
print("Bienvenido, vamos a calcular su sueldo dependiendo de la categoría en la que se encuentre")
while repetir:
    categoria = int(input("Selecciona su categoría:\n0.Salir\n1.Categoría 1\n2.Categoría 2\n3.Categoria 3\n4.Categoria 4\n"))
    match categoria:
        case 0:
            print("Gracias por usar este programa...")
            repetir = False
        case 1:
            nombre = input("Diga su nombre:\n")
            edad = int(input("Diga su edad:\n"))
            anios = int(input("Años trabajados en la empresa:\n"))
            horasExtras = int(input("¿Cuántas horas extras has hecho este mes?\n"))

            if horasExtras>maxHorasExtras:
                sueldo = salarioBase + maxHorasExtras*dineroExtraHora1
            else:
                sueldo = salarioBase + horasExtras*dineroExtraHora1
           
            while anios != 0:
                if anios%3==0:
                    sueldo = sueldo + sueldo*porcentajeAnt/100
                anios -=1
               
               
            if edad == 25:
                sueldo = sueldo + sueldo*porcentajeEdad/100

            print(f'Su sueldo es de {sueldo:.2f} €')
        case 2:

            nombre = input("Diga su nombre:\n")
            edad = int(input("Diga su edad:\n"))
            anios = int(input("Años trabajados en la empresa:\n"))
            horasExtras = int(input("¿Cuántas horas extras has hecho este mes?\n"))

            if horasExtras>maxHorasExtras:
                sueldo = salarioBase + maxHorasExtras*dineroExtraHora2
            else:
                sueldo = salarioBase + horasExtras*dineroExtraHora2
           
            while anios != 0:
                if anios%3==0:
                    sueldo = sueldo + sueldo*porcentajeAnt/100
                anios -=1
               
            if edad == 25:
                sueldo = sueldo + sueldo*porcentajeEdad/100

            print(f'Su sueldo es de {sueldo:.2f} €')
        case 3:
            nombre = input("Diga su nombre:\n")
            edad = int(input("Diga su edad:\n"))
            anios = int(input("Años trabajados en la empresa:\n"))
            horasExtras = int(input("¿Cuántas horas extras has hecho este mes?\n"))

            if horasExtras>maxHorasExtras:
                sueldo = salarioBase + maxHorasExtras*dineroExtraHora3
            else:
                sueldo = salarioBase + horasExtras*dineroExtraHora3
           
            while anios != 0:
                if anios%3==0:
                    sueldo = sueldo + sueldo*porcentajeAnt/100
                anios -=1
               
               
            if edad == 25:
                sueldo = sueldo + sueldo*porcentajeEdad/100

            print(f'Su sueldo es de {sueldo:.2f} €')
        case 4:
            nombre = input("Diga su nombre:\n")
            edad = int(input("Diga su edad:\n"))
            anios = int(input("Años trabajados en la empresa:\n"))
           
            sueldo = salarioBase
            while anios != 0:
                if anios%3==0:
                    sueldo = sueldo + sueldo*porcentajeAnt/100
                anios -=1
               
               
            if edad == 25:
                sueldo = sueldo + sueldo*porcentajeEdad/100

            print(f'Su sueldo es de {sueldo:.2f} €')
        case _:
            print("Hubo un error al elegir la categoría")
