import math
class Figura:
    
    def __init__(self,nombre:str):
        
        self.nombre=nombre
        
    
    def calcularArea (self):
        
        pass
    
    def calcularPerimetro (self):
        pass
    
    
    
    

class Rectangulo(Figura):
    
    def __init__(self, nombre:str,base:float,altura:float):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def calcularArea(self)->float:
        
        return self.base*self.altura
    
    def calcularPerimetro(self)->float:
        
        return (self.base+self.altura)*2
    
    

class Triangulo(Figura):
    
    def __init__(self, nombre:str,base:float,altura:float):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
        
    def __str__(self):
        return f'figura(Nombre: {self.nombre}, Altura: {self.altura}, Base: {self.base})'
    
    def calcularArea(self):
        
        return self.base*2*self.altura/2
    

    def calcularPerimetro(self):
        
        return self.base*3

class Circulo(Figura):
    
    def __init__(self, nombre,radio:float):
        super().__init__(nombre)
        self.radio=radio
        
    
    def calcularArea(self):
        return math.pi*self.radio**2
    
    def calcularPerimetro(self):
        
        return 2*math.pi*self.radio
    
 

figuras: list [Figura] =[
    
    Rectangulo('Rectangulo',5,5),
    
    Circulo('Circulo',5),
    
    Triangulo('Triangulo',6,5),
    
    Rectangulo('Rectangulo',10,8),
    
    Circulo('Circulo',3),
    
    Triangulo('Triangulo',4,7),
    
    Rectangulo('Rectangulo',7,12),
    
    Circulo('Circulo',6.5),
    
    Triangulo('Triangulo',8,9)
]

suma = 0.0
perimetro = 0.0
area = 0.0
triangulo = None

suma = sum(i.calcularArea() for i in figuras)

print(f'El area de todas las figuras es: {suma:.2f} metros')

perimetro = sum(i.calcularPerimetro() for i in figuras)

print(f'La suma de todos los perimetros es {perimetro:.2f} metros')

for i in figuras:
    if isinstance (i,Triangulo):
        if area<i.calcularArea():
            area = i.calcularArea()
            triangulo=i

print(f'El triangulo con mayor area es {triangulo}') 