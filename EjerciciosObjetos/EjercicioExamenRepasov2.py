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
    
    
    def calcularCosteTotal(self,Servidores:list[Servidor]):
        
        total = 0.0
        for servidor in Servidores:
            total = total + servidor.calcular_coste_base()
            
        return total
    
    def calcularDescuento (self, servidores:list[Servidor],umbralDescuento:float,descuento:float)->float:
        basePorcentaje :float = 100
        total : float = CentroDeServidores.calcularCosteTotal(servidores)
        
        if total > umbralDescuento:
            return total - ((total*descuento)/basePorcentaje)
        return total
    @staticmethod
    def calcularCosteUnicoMMO(self, servidores:list[Servidor])-> float:
      servidoresFiltrado =[servidor for servidor in servidores if isinstance(servidor,MMO)]
      return self.calcularCosteTotal(servidoresFiltrado)
  
    
    @staticmethod
    def calcularCosteStreaming(self, servidores:list[Servidor])->float:
        servidoresFiltrado = [servidor for servidor in servidores if isinstance(servidor,Streaming)]
        return CentroDeServidores.calcularCosteTotal(servidoresFiltrado)
    
class CloudHostingMixin():
    
    def __init__(self,gigaByte:int, costeGb:float):
        self.gigaByte = gigaByte
        self.costeGb = costeGb
        
    def annadirGb(self,costeOriginal:float):
        return costeOriginal +(self.gigaByte * self.costeGb)

class BackupMixin():
    
    frecuenciaBackup = 7
    
    def __init__(self, costeBackup:float):
        self.costeBackup = costeBackup
    
    def annadirBackup(self, costeOriginal:float, diasActivo:int):
        return costeOriginal+((diasActivo//BackupMixin.frecuenciaBackup)*self.costeBackup)
    
class ServidorHibrido(MMO,BattleRoyale):
    
    def __init__(self, nombre, costDiario, costAct):
        super().__init__(nombre, costDiario, costAct)
    
    
    
        