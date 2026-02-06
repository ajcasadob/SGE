class Animales:
    
    def __init__(self,nombre:str, coste:float):
        self.nombre = nombre
        self.coste = coste
        
    def calcularCoste(self, numDiasAnio: int) -> float:
        return self.coste * numDiasAnio