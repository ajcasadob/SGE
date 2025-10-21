maxHorasExtras = 30.0
dineroExtraHora1 = 40.0
dineroExtraHora2 = 50.0
dineroExtraHora3 = 75.0
porcentajeAnt = 2.0
porcentajeEdad = 4.0
salarioBase = 1300.0
repetir = True

while repetir:

    op = int(input("0.Salir\n1.Calcular sueldo"))
    match op:
        case 0:
            print("Saliendo...")
            repetir = False
        case 1:
            cat = int(input("Selecciona su categoría:\n1.Cat 1\n2.Cat 2\n3.Cat 3\n4.Cat 4"))
            match cat:
                case 1:
                    dineroExtra = dineroExtraHora1
                case 2:
                    dineroExtra = dineroExtraHora2
                case 3:
                    dineroExtra = dineroExtraHora3
                case 4:
                    print("Al ser de categoría 4 no tiene paga extra por horas")

            if cat != 4:
                horasExtras = float(input("Horas extras:\n"))
                if horasExtras>maxHorasExtras:
                    sueldo = salarioBase + dineroExtra*maxHorasExtras
                else:
                    sueldo = salarioBase + dineroExtra*horasExtras
            else:
                sueldo = salarioBase

            anios = int(input("Años en la empresa:"))

            sueldo = sueldo + (sueldo*(anios//3)*porcentajeAnt/100.0)

            if anios == 25:
                sueldo = sueldo + sueldo*porcentajeEdad/100.0

            print(f'Su sueldo es {sueldo:.2f}')