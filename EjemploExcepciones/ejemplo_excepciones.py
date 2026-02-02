def intdiv(a:int, b:int)->int:
    try:
        result =  a //b
    except TypeError:
        print('Operador erroneo')
    except ZeroDivisionError:
        print('No se puede dividi por zero')
    except Exception:
        print('Algo ocurrio malamente')

intdiv(3,'gg')


def intdiv3 (a:int, b:int)->int:
    try:
        result = a // b
    except (TypeError, ZeroDivisionError):
        print('Observa las operaciones, algo esta causando errores')
    except Exception:
        print('Algo salio mal')
        

intdiv3(3,0)

values = [4,2,7]
try:
    r = values[3]
except IndexError:
    print('Error indice no esta en la lista')
else:
    print(f'Tu indice buscado es{r}')
finally:
    print('Que tengas un buen dia')
    
    
try:
    print(values[3])
except IndexError as err:
    print(f'Algo salio mal: {err}')


def getint(a):
    try:
        result = int(a)  
        return result
    except ValueError:
        print('Tiene que ser un numero entero')
    except Exception:
        print('Algo salio mal')

getint('hola')  