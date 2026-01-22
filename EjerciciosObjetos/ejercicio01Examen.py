class yogur:
    
    capacidad:float = 100.0
    calorias:float = 120.5
    
    def __init__(self,sabor:str,marca:str,trocitos:bool,desnatado:bool):
        self._sabor=sabor
        self._marca=marca
        self._trocitoss=trocitos
        self._desnatado=desnatado
    
    @property
    def sabor(self):
        return self._sabor
    
    @sabor.setter
    def sabor(self, sabor:str):
        self._sabor = sabor
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca:str):
        self._marca = marca
    
    @property
    def trocitoss(self):
        return self._trocitoss
    
    @trocitoss.setter
    def trocitoss(self, trocitos:bool):
        self._trocitoss = trocitos
    
    @property
    def desnatado(self):
        return self._desnatado
    
    @desnatado.setter
    def desnatado(self, desnatado:bool):
        self._desnatado = desnatado
        
class Calorias:
    
    def calcularCalorias(yogur:yogur, tamanio:float)->float:
        calorias = 0.0
        if yogur.desnatado:
            calorias = (tamanio * yogur.calorias) / yogur.capacidad
            calorias = calorias - calorias*30/100
        else:
            calorias = (tamanio * yogur.calorias) / yogur.capacidad    
        return calorias
    
    def sumarCalorias(yogures:list[yogur],tamanios:list[float]):
        suma = 0
        for i in range(len(yogures)):
            suma += Calorias.calcularCalorias(yogures[i],tamanios[i])
        return suma
    
    def calcularCaloriasTipo(yogures:list[yogur], tamanio:float):
    
        resultado = 0
        for i in yogures:
            if i.desnatado:
                resultado += Calorias.calcularCalorias(i,tamanio)
        return resultado


class Principal:
    
        cantidad = int(input("¿Cuántos yogures vas a agregar? "))
        
        yogures = []
        tamanios = []
        
        for i in range(cantidad):
            print(f"\nYogur {i+1}")
            sabor = input("Introduce el sabor: ")
            marca = input("Introduce la marca: ")
            trocitos = input("¿Tiene trocitos? (s/n): ").lower() == 's'
            desnatado = input("¿Es desnatado? (s/n): ").lower() == 's'
            tamanio = float(input("Tamaño en ml: "))
            
            mi_yogur = yogur(sabor, marca, trocitos, desnatado)
            yogures.append(mi_yogur)
            tamanios.append(tamanio)
            
            calorias = Calorias.calcularCalorias(mi_yogur, tamanio)
            print(f"Calorías del yogur {i+1}: {calorias} kcal")
        
        
        total_calorias = Calorias.sumarCalorias(yogures, tamanios)
        
        print(f"\nTotal de calorías de todos los yogures: {total_calorias} kcal")
        
        total_desnatado = Calorias.calcularCaloriasTipo(yogures, 100)
        print(f"Calorías solo de yogures desnatados (100ml c/u): {total_desnatado} kcal")

