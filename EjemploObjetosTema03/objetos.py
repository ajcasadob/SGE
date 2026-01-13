from __future__ import annotations

class StarWarsDroid:
    pass
c3po = StarWarsDroid()
r2d2 = StarWarsDroid()
bb8 = StarWarsDroid()    




##Metodo decorador, con esto conseguimos cambiar la funcion del metodo sin alterar su codigo
class Droid:
    @staticmethod
    def audit (method):
        def wrapper (self, *args, **kwargs):
            print(f'Droid {self.name} running {method.__name__}')
            return method(self, *args, **kwargs)
        return wrapper
    
    def __init__(self, name: str):
        self.name = name
        self.pos = [0,0]
        
    @audit
    def move (self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y
    
    @audit
    def reset (self):
        self.pos = [0,0]
##El decorador se puede poner dentro o fuera de la clase, por una cuestion de encapsulamiento 
# tendria sentido dejarlo dentro de la clase como metodo estatico.


##METODOS MAGICOS

##Los metodos magicos se disparan de manera transparente cuando utilizamos ciertas estructuras y expresiones del lenguaje.

## A continucion muestro una equivalencia  entre operadores y metodos magicos
## __eq__ es lo mismo que ==

class Droid:
    def __init__ ( self, name: str, serial_number: int):
        self.name = name
        self.serial_number= serial_number
        
    def __eq__(self, droid: Droid)-> bool:
        return self.name == droid.name
    
    
    droid1 = Droid('C-3PO')
    droid2 = Droid('C-3PO')
    
    print(droid1 == droid2)
    
    droid1 = Droid('C-3P4')
    droid2 = Droid('C-3PO')
    
    droid1.__eq__(droid2)
    
##Existen muchos otros en la documentacion oficial de Pyhton

##Veamos un ejemplo donde sumamos dos droides

class Droid:
    
    def __init__(self, name: str, power:int):
        self.name = name
        self.power = power
        
    def __ad__(self, other: Droid)-> Droid:
        new_name = self.name + '-' + other.name
        new_power = self.power + other.power
        return Droid(new_name, new_power)
    