def validar_horas(func):
    def wrapper(self,precio_base_hora:float):
        if self.horas_estacionada < 0:
            raise ValueError (f'Las horas no pueden ser negativas:{self.horas_estacionada}')
        return func(self, precio_base_hora)
    return wrapper


class Vehiculo:
    
    def __init__(self,matricula:str,horas_estacionada:float):
        self.matricula = matricula
        self.horas_estacionada = horas_estacionada
        
    
    def calcular_coste(self, precio_base_hora:float):
        return precio_base_hora*self.horas_estacionada
    
    def __str__(self):
        return f"{self.matricula}{self.horas_estacionada}"
    
    def __eq__(self, otro):
        if isinstance(otro,Vehiculo):
            return self.matricula == otro.matricula
        return False
        
        

class Coche(Vehiculo):
        
        @validar_horas 
        def calcular_coste(self, precio_base_hora):
            return Vehiculo.calcular_coste(self,precio_base_hora)*1
        

class Moto(Vehiculo):
    

    @validar_horas
    def calcular_coste(self, precio_base_hora):
        return Vehiculo.calcular_coste(self,precio_base_hora)*0.75
    

class Furgoneta(Vehiculo):
    
    @validar_horas
    def calcular_coste(self, precio_base_hora):
        return Vehiculo.calcular_coste(self,precio_base_hora)*1.5
    

class VehiculoElectricoMixin:
    
    def aplicar_descuento_electrico(self,coste:float):
        return coste*0.9
    

class CocheElectrico(Coche, VehiculoElectricoMixin):
    
    def calcular_coste(self, precio_base_hora):
        coste_base=  Coche.calcular_coste(self,precio_base_hora)
        return self.aplicar_descuento_electrico(coste_base)
        

class FurgonetaElectrica(Furgoneta, VehiculoElectricoMixin):
    
    def calcular_coste(self, precio_base_hora):
        coste_base=Furgoneta.calcular_coste(self,precio_base_hora)
        return self.aplicar_descuento_electrico(coste_base)
    
    
class Estacionamiento:
    
    def __init__(self,precio_base_hora:float):
        self.vehiculos=[]
        self.precio_base_hora=precio_base_hora
        
    def anadir_vehiculo(self, vehiculo:Vehiculo):
        self.vehiculos.append(vehiculo)
        
    def calcular_coste_total(self):
        total = 0.0
        for vehiculo in self.vehiculos:
            total += vehiculo.calcular_coste(self.precio_base_hora)
        return total
            
    def contar_vehiculo_por_tipo(self):
        conteo= {}
        for vehiculo in self.vehiculos:
            tipo = type(Vehiculo).__name__
            conteo[tipo] = conteo.get(tipo,0)+1
        return conteo
    
    def __len__(self):
        return len(self.vehiculos)
    
    def __contains__(self,matricula:str):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                return True
        return False

if __name__ == "__main__":
    print("=== ESTACIONAMIENTO - PRUEBAS ===\n")
    
   
    parking = Estacionamiento(precio_base_hora=10)
    
   
    coche1 = Coche("ABC123", 5)
    coche2 = Coche("DEF456", 3)
    moto1 = Moto("XYZ789", 4)
    furgoneta1 = Furgoneta("FUR999", 6)
    coche_electrico = CocheElectrico("ELE001", 5)
    furgoneta_electrica = FurgonetaElectrica("ELEF002", 4)
   
    parking.anadir_vehiculo(coche1)
    parking.anadir_vehiculo(coche2)
    parking.anadir_vehiculo(moto1)
    parking.anadir_vehiculo(furgoneta1)
    parking.anadir_vehiculo(coche_electrico)
    parking.anadir_vehiculo(furgoneta_electrica)
    
   
    print(f"Total de vehículos: {len(parking)}\n")
    
    
    print(f"Coste total: {parking.calcular_coste_total():.2f}€\n")
    
    
    print("Vehículos por tipo:")
    conteo = parking.contar_vehiculo_por_tipo()
    for tipo, cantidad in conteo.items():
        print(f"  {tipo}: {cantidad}")
    print()
    
    
    print("Prueba de búsqueda por matrícula:")
    print(f"  ¿'ABC123' en parking? {('ABC123' in parking)}")
    print(f"  ¿'ZZZ999' en parking? {('ZZZ999' in parking)}\n")
    
    
    print("Prueba de métodos mágicos de Vehiculo:")
    print(f"  {coche1}")
    print(f"  ¿coche1 == coche2? {coche1 == coche2}")
    coche_copia = Coche("ABC123", 10)
    print(f"  ¿coche1 == coche_copia (misma matrícula)? {coche1 == coche_copia}\n")
    
    
    print("Prueba del decorador (horas negativas):")
    try:
        coche_invalido = Coche("BAD999", -5)
        coche_invalido.calcular_coste(10)
    except ValueError as e:
        print(f"   Error capturado: {e}")
