repetir = True

f= open('inventario.txt','r')

while repetir:
    
    el = int(input('''
0. Salir
1. Listar inventario
2. Añadir piezas
3. Buscar piezas
4. Eliminar pieza
5. Editar pieza
'''))
    
    match el:
        
        case 0:
            
            repetir =False
            print('Gracias por elegir mi programa')
            
        case 1:
            f.seek(0)
            contenido = f.read()
            print(contenido)
            
        case 2:
            codigo = input('Ingrese el código de la pieza: ')
            nombre = input('Ingrese el nombre de la pieza: ')
            cantidad = input('Ingrese la cantidad: ')
            precio = input('Ingrese el precio: ')
            categoria = input('Ingrese la categoría: ')
            
            with open('inventario.txt', 'a') as fa:
                fa.write(f'{codigo}|{nombre}|{cantidad}|{precio}|{categoria}\n')
            
            print('Pieza añadida correctamente')
            
        case 3:
            busqueda = input('Ingrese el código o nombre de la pieza a buscar: ')
            f.seek(0)
            encontrado = False
            
            for linea in f:
                if busqueda.lower() in linea.lower():
                    print(linea.strip())
                    encontrado = True
            
            if not encontrado:
                print('No se encontró ninguna pieza con ese criterio')
                
        case 4:
            codigo_eliminar = input('Ingrese el código de la pieza a eliminar: ')
            f.seek(0)
            lineas = f.readlines()
            
            with open('inventario.txt', 'w') as fw:
                eliminado = False
                for linea in lineas:
                    if not linea.startswith(codigo_eliminar + '|'):
                        fw.write(linea)
                    else:
                        eliminado = True
                
                if eliminado:
                    print('Pieza eliminada correctamente')
                else:
                    print('No se encontró ninguna pieza con ese código')
        case 5:
            codigo_editar = input('Ingrese el código de la pieza a editar: ')
            f.seek(0)
            lineas = f.readlines()
            
            with open('inventario.txt', 'w') as fw:
                editado = False
                for linea in lineas:
                    if linea.startswith(codigo_editar + '|'):
                        print(f'Pieza encontrada: {linea.strip()}')
                        nombre = input('Ingrese el nuevo nombre (o Enter para mantener): ')
                        cantidad = input('Ingrese la nueva cantidad (o Enter para mantener): ')
                        precio = input('Ingrese el nuevo precio (o Enter para mantener): ')
                        categoria = input('Ingrese la nueva categoría (o Enter para mantener): ')
                        
                        partes = linea.strip().split('|')
                        nuevo_nombre = nombre if nombre else partes[1]
                        nueva_cantidad = cantidad if cantidad else partes[2]
                        nuevo_precio = precio if precio else partes[3]
                        nueva_categoria = categoria if categoria else partes[4]
                        
                        fw.write(f'{codigo_editar}|{nuevo_nombre}|{nueva_cantidad}|{nuevo_precio}|{nueva_categoria}\n')
                        editado = True
                        print('Pieza editada correctamente')
                    else:
                        fw.write(linea)
                
                if not editado:
                    print('No se encontró ninguna pieza con ese código')
        
        case _:
            print('La opción elegida no existe, intentelo de nuevo')            
f.close()