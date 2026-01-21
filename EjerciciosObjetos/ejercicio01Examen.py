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
    
    def sumarCalorias(yogures:list[yogur],tamanio:float):
        suma = 0
        for i in yogures:
            suma += Calorias.calcularCalorias(i,tamanio)
        return suma
    
    def calcularCaloriasTipo(yogures:list[yogur], tamanio:float):
    
        resultado = 0
        for i in yogures:
            if i.desnatado:
                resultado += Calorias.calcularCalorias(i,tamanio)
        return resultado


class Principal:
    
    
        print("Primer yogur")
        sabor = input("Introduce el sabor: ")
        marca = input("Introduce la marca: ")
        trocitos = input("¿Tiene trocitos? (s/n): ").lower() == 's'
        desnatado = input("¿Es desnatado? (s/n): ").lower() == 's'
        tamanio = float(input("Tamaño en ml: "))
        
        
        mi_yogur = yogur(sabor, marca, trocitos, desnatado)
        calorias_yogur1 = Calorias.calcularCalorias(mi_yogur, tamanio)
        print(f"Calorías del yogur: {calorias_yogur1} kcal\n" )
        
        print("Segundo yogur")
        
        sabor2= input("Introduce el sabor: ")
        marca2= input("Introduce la marca: ")
        trocitos2= input("¿Tiene trocitos ? (s/n): ").lower() == 's'
        desnatado2 = input("¿Es desnatado ? (s/n): ").lower() == 's'
        tamnio2= float(input("Tamaño en ml:"))
        
        mi_yogur2= yogur(sabor2,marca2,trocitos2,desnatado2)
        calorias_yogur2 = Calorias.calcularCalorias(mi_yogur2,tamnio2)
        
        print(f"\nCalorías del yogur: {calorias_yogur2} kcal\n")
        
        yogures = [mi_yogur,mi_yogur2]
        
        total = Calorias.sumarCalorias(yogures,100)
        print(f"Calorias totales de los yogures (100ml c/u): {total} kcal")
        
        total_desnatado = Calorias.calcularCaloriasTipo(yogures, 100)
        print(f"Calorías solo de yogures desnatados (100ml c/u): {total_desnatado} kcal")

