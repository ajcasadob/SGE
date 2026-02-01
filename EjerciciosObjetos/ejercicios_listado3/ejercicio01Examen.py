class Yogur:
    capacidad = 100.0         
    calorias_base = 120.5      

    def __init__(self, sabor, marca, trocitos):
        self._sabor = sabor
        self._marca = marca
        self._trocitos = trocitos

    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, sabor):
        self._sabor = sabor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def trocitos(self):
        return self._trocitos

    @trocitos.setter
    def trocitos(self, trocitos):
        self._trocitos = trocitos

    def tipo(self):
        return "normal"

    def calorias(self, tamanio_ml):
        """Calorías de este yogur para un tamaño dado (en ml)."""
        return (tamanio_ml * self.calorias_base) / self.capacidad


class YogurDesnatado(Yogur):
    def __init__(self, sabor, marca, trocitos, porcentaje_reduccion=30.0):
        super().__init__(sabor, marca, trocitos)
        self._porcentaje_reduccion = porcentaje_reduccion

    def tipo(self):
        return "desnatado"

    def calorias(self, tamanio_ml):
        calorias_normales = super().calorias(tamanio_ml)
        reduccion = calorias_normales * self._porcentaje_reduccion / 100
        return calorias_normales - reduccion


class YogurProteinas(Yogur):
    def __init__(self, sabor, marca, trocitos, extra_proteina):
        super().__init__(sabor, marca, trocitos)
        self._extra_proteina = extra_proteina

    def tipo(self):
        return "proteinas"

    def calorias(self, tamanio_ml):
        calorias_normales = super().calorias(tamanio_ml)
        extra = (tamanio_ml * self._extra_proteina) / self.capacidad
        return calorias_normales + extra


class Calorias:
    @staticmethod
    def calcular_calorias_yogur(yogur, tamanio_ml):
        return yogur.calorias(tamanio_ml)

    @staticmethod
    def sumar_calorias(yogures, tamanios_ml):
        """Suma calorías de varios yogures, mismo índice en listas."""
        suma = 0.0
        for i in range(len(yogures)):
            suma = suma + yogures[i].calorias(tamanios_ml[i])
        return suma

    @staticmethod
    def calorias_por_tipo(yogures, tamanios_ml, tipo_buscado):
        """
        Suma solo las calorías de los yogures de un tipo concreto
        (normal, desnatado, proteinas) según yogur.tipo().
        """
        suma = 0.0
        for i in range(len(yogures)):
            if yogures[i].tipo() == tipo_buscado:
                suma = suma + yogures[i].calorias(tamanios_ml[i])
        return suma




cantidad = int(input("¿Cuántos yogures vas a agregar? "))

yogures = []
tamanios = []

for i in range(cantidad):
    print(f"\nYogur {i + 1}")
    sabor = input("Introduce el sabor: ")
    marca = input("Introduce la marca: ")
    trocitos = input("¿Tiene trocitos? (s/n): ").lower() == "s"

    print("Tipo de yogur:")
    print("1. Normal")
    print("2. Desnatado")
    print("3. Proteínas")
    opcion_tipo = int(input("Elige tipo (1-3): "))

    tamanio = float(input("Tamaño en ml: "))

    if opcion_tipo == 1:
        mi_yogur = Yogur(sabor, marca, trocitos)
    elif opcion_tipo == 2:
       
        mi_yogur = YogurDesnatado(sabor, marca, trocitos, 30.0)
    else:
        
        extra = float(input("Calorías extra por proteínas (por 100 ml): "))
        mi_yogur = YogurProteinas(sabor, marca, trocitos, extra)

    yogures.append(mi_yogur)
    tamanios.append(tamanio)

    calorias_yogur = Calorias.calcular_calorias_yogur(mi_yogur, tamanio)
    print(f"Calorías del yogur {i + 1}: {calorias_yogur:.2f} kcal")


total_calorias = Calorias.sumar_calorias(yogures, tamanios)
print(f"\nTotal de calorías de todos los yogures: {total_calorias:.2f} kcal")

calorias_desnatados = Calorias.calorias_por_tipo(yogures, tamanios, "desnatado")
print(f"Calorías solo de yogures desnatados: {calorias_desnatados:.2f} kcal")

calorias_proteinas = Calorias.calorias_por_tipo(yogures, tamanios, "proteinas")
print(f"Calorías solo de yogures de proteínas: {calorias_proteinas:.2f} kcal")
