class Vehiculo:
    
    def __init__(self,matricula:str,marca:str,litros:float):
        self.matricula = matricula
        self.marca = marca
        self.litros = litros
        
    def costeRecorrido(self,km:float)->float:
        return self.litros*km
    
    def __str__(self):
        return f"{self.marca}, {self.matricula}"

class Electrico(Vehiculo):
        
        def __init__(self, matricula, marca, litros,cost:float):
            Vehiculo.__init__(self,matricula, marca, litros)
            self.cost = cost
            

        def costeRecorrido(self, km):
            return super().costeRecorrido(km)+self.cost
        
        def __str__(self):
            return super().__str__()
        
        
class Autonomo(Vehiculo):
    
    def __init__(self, matricula, marca, litros,costSistema:float):
        Vehiculo.__init__(self,matricula, marca, litros)
        self.costSistema = costSistema
        
    def costeRecorrido(self, km):
        return super().costeRecorrido(km)+self.costSistema
    
    def __str__(self):
        return super().__str__()

class CocheInteligente(Electrico, Autonomo):
    
    def __init__(self, matricula, marca, litros, cost,costSistema):
        Electrico.__init__(self,matricula, marca, litros, cost)
        Autonomo.__init__(self,matricula, marca, litros,costSistema)
    
    def costeRecorrido(self, km):
        return super().costeRecorrido(km)+Autonomo.costeRecorrido(self,km)
    

class Principal:
    
        cantidad = int(input("¿Cuántos vehiculos vas a agregar? "))
        
        
        
        for i in range(cantidad):
            print(f"\nCoche {i+1}")
            matricula = input("Introduce la matricula: ")
            marca = input("Introduce la marca: ")
            litros = float(input("Litros de consumo: "))
            cost = float(input('Coste adicional:'))
            
        vehiculos = []
        miVehiculo= Vehiculo(matricula,marca,litros)
        ci = CocheInteligente(matricula,marca,litros,cost,5)
        c2 = Electrico(matricula,marca,litros,cost)
        vehiculos.append(miVehiculo)
        vehiculos.append(ci)
        
        kms = float(input('Kms recorridos: '))
        miVehiculo.costeRecorrido(kms)
        
        print(miVehiculo.costeRecorrido(kms))
        print(ci.costeRecorrido(kms))
        print(c2.costeRecorrido(kms))
        
        
            
        print(miVehiculo)