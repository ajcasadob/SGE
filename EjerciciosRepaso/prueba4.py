maxHorasExtras = 30.0
dineroExtraHora1 = 40.0
dineroExtraHora2 = 50.0
dineroExtraHora3 = 75.0
porcentajeAnt = 2.0
porcentajeEdad = 4.0
salarioBase = 1300.0
repetir = True

while repetir:

    op = int(input("Elige la opcion: 1.Calcular sueldo \n0.Salir\n"))

    match op:

        case 0:
            print('Saliendo..')
            repetir = False

        case 1:
            cat = int(input("Elige la categoria que desee: 1.Categoria 1 \n2.Categoria 2 \n3.Categoria 3 \n4.Categoria 4\n"))

            match cat:
                case 1:
                    dineroExtra = dineroExtraHora1
                case 2:
                    dineroExtra = dineroExtraHora2
                case 3:
                    dineroExtra = dineroExtraHora3
                case 4:
                    print('La categoria 4 no tiene hora extra')
                    dineroExtra = 0

            # Calcular horas extras solo si aplica
            if dineroExtra > 0:
                horasExtras = float(input('Ingrese las horas extras trabajadas: '))
                if horasExtras > maxHorasExtras:
                    sueldo = salarioBase + dineroExtra * maxHorasExtras
                else:
                    sueldo = salarioBase + dineroExtra * horasExtras
            else:
                sueldo = salarioBase

            anios = int(input('Ingrese los años en la empresa: '))
            sueldo += (sueldo * (anios // 3) * porcentajeAnt / 100.0)

            if anios == 25:
                sueldo += sueldo * porcentajeEdad / 100.0

            print(f'Su sueldo es {sueldo:.2f}')
