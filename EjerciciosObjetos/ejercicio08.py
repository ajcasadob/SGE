import math
class Figura:
    
    def calcularArea (self):
        
        pass
    
    def calcularPerimetro (self):
        pass
    
    
    
    pass

class Rectangulo(Figura):
    
    def calcularArea(base:float, altura:float):
        
        return base*altura
    
    def calcularPerimetro(base:float, altura:float):
        
        return (base+altura)*2
    
    pass

class Triangulo(Figura):
    
    def calcularArea(base:float, altura:float):
        
        return base*2*altura/2
    pass

    def calcularPerimetro(longitudUno:float,longitudDos:float, longitudTres:float):
        return longitudUno+longitudDos+longitudTres

class Circulo(Figura):
    
    def calcularArea(radio:float):
        return math.pi*radio**2
    pass