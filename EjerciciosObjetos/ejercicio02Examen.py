class Animales:
    
    def __init__(self,nombre:str,coste:float):
        self.nombre= nombre
        self.coste = coste
        
    def calcularCoste(self,numDiasAnios:int) -> float:
        return self.coste*numDiasAnios
    
    
    
class Osos(Animales):
    
    def __init__(self, nombre, coste:float,precioCarnePescado:float):
        super().__init__(nombre, coste)
        self.precioCarnePescado = precioCarnePescado
        
        
    def calcularCoste(self, numDiasAnios):
        semanasAnios = 52
        return (self.precioCarnePescado*2*semanasAnios)+super().calcularCoste(numDiasAnios)
    
class Serpientes(Animales):
    
    def __init__(self, nombre:str, coste:float, numInsectos:int, precioInsecto:float):
        super().__init__(nombre, coste)
        self.numInsesctos = numInsectos
        self.precioInsecto = precioInsecto
        
    def calcularCoste(self, numDiasAnios):
        semanasAnios = 52
        return (self.numInsesctos*self.precioInsecto*2*semanasAnios)+super().calcularCoste(numDiasAnios)
    
    
    