class Servidor:
    
    def __init__(self,nombre:str,costDiario:float,):
        self.nombre = nombre
        self.costDiario = costDiario

    def calcular_coste_base(self,):
        dias = 365
        return dias*self.costDiario
    
    
    
class MMO(Servidor):
    
    def __init__(self, nombre, costDiario,costAct:float):
        super().__init__(nombre, costDiario)
        self.costAct = costAct
        
        
    def calcular_coste_base(self):
        return super().calcular_coste_base()+self.costAct*12
    
class BattleRoyale(Servidor):
    
    def __init__(self, nombre, costDiario,costMant:float):
        super().__init__(nombre, costDiario)
        self.costMan = costMant
        
        
    def calcular_coste_base(self):
        return super().calcular_coste_base()+3*self.costMan*52
    
class Streaming(Servidor):
    
    def __init__(self, nombre, costDiario,mediaUsu:float,costUsu:float):
        super().__init__(nombre, costDiario)
        self.mediaUsu = mediaUsu
        self.costUsu = costUsu
        
    def calcular_coste_base(self):
        return super().calcular_coste_base()+self.costUsu*self.mediaUsu

class CentroDeServidores:
    
    def calcularCosteDescuento(self,func):
        def wrrapper (self, Servidores:list[Servidor],cantMin:float,descuento:float, *args, **kwargs):
    
    
    
    
    def calcularCosteTotal(self,Servidores:list[Servidor]):
        
        total = 0.0
        for servidor in Servidores:
            total = total + servidor.calcular_coste_base()
            
        return total

    
    
        