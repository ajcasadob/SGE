

def validar_tamanio_minimo(func):
    def envoltura(self, tamanio_ml, *args, **kwargs):
        if tamanio_ml < 50:
            print(f"Tamaño {tamanio_ml} ml demasiado pequeño, se ajusta a 50 ml.")
            tamanio_ml = 50
        return func(self, tamanio_ml, *args, **kwargs)
    return envoltura


def comprobar_es_yogur(func):
    def envoltura(self, *args, **kwargs):
        if not getattr(self, "es_yogur", True):
            print("ATENCIÓN: Esto no es un yogur, es un postre lácteo.")
        return func(self, *args, **kwargs)
    return envoltura



class Yogur:
    capacidad = 100.0
    calorias_base = 120.5

    def __init__(self, sabor, marca, trocitos, es_yogur=True):
        self._sabor = sabor
        self._marca = marca
        self._trocitos = trocitos
        self.es_yogur = es_yogur

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

    @comprobar_es_yogur
    @validar_tamanio_minimo
    def calorias(self, tamanio_ml):
        return (tamanio_ml * self.calorias_base) / self.capacidad

    
    def __eq__(self, otro):
        if not isinstance(otro, Yogur):
            return False
        tamaño_prueba = 100.0
        return self.calorias(tamaño_prueba) == otro.calorias(tamaño_prueba)


class YogurDesnatado(Yogur):
    def __init__(self, sabor, marca, trocitos, porcentaje_reduccion=30.0, es_yogur=True):
        super().__init__(sabor, marca, trocitos, es_yogur)
        self._porcentaje_reduccion = porcentaje_reduccion

    def tipo(self):
        return "desnatado"

    @comprobar_es_yogur
    @validar_tamanio_minimo
    def calorias(self, tamanio_ml):
        calorias_normales = (tamanio_ml * self.calorias_base) / self.capacidad
        reduccion = calorias_normales * self._porcentaje_reduccion / 100
        return calorias_normales - reduccion


class YogurProteinas(Yogur):
    def __init__(self, sabor, marca, trocitos, extra_proteina, es_yogur=True):
        super().__init__(sabor, marca, trocitos, es_yogur)
        self._extra_proteina = extra_proteina

    def tipo(self):
        return "proteinas"

    @comprobar_es_yogur
    @validar_tamanio_minimo
    def calorias(self, tamanio_ml):
        calorias_normales = (tamanio_ml * self.calorias_base) / self.capacidad
        extra = (tamanio_ml * self._extra_proteina) / self.capacidad
        return calorias_normales + extra



class Calorias:
    @staticmethod
    def calcular_calorias_yogur(yogur, tamanio_ml):
        return yogur.calorias(tamanio_ml)

    @staticmethod
    def sumar_calorias(yogures, tamanios_ml):
        suma = 0.0
        for i in range(len(yogures)):
            suma = suma + yogures[i].calorias(tamanios_ml[i])
        return suma

    @staticmethod
    def calorias_por_tipo(yogures, tamanios_ml, tipo_buscado):
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

    
    es_yogur_resp = input("¿Es realmente un yogur (fermentado)? (s/n): ").lower()
    es_yogur = es_yogur_resp == "s"

    print("Tipo de producto:")
    print("1. Normal")
    print("2. Desnatado")
    print("3. Proteínas")
    opcion_tipo = int(input("Elige tipo (1-3): "))

    tamanio = float(input("Tamaño en ml: "))

    if opcion_tipo == 1:
        mi_yogur = Yogur(sabor, marca, trocitos, es_yogur)
    elif opcion_tipo == 2:
        mi_yogur = YogurDesnatado(sabor, marca, trocitos, 30.0, es_yogur)
    else:
        extra = float(input("Calorías extra por proteínas (por 100 ml): "))
        mi_yogur = YogurProteinas(sabor, marca, trocitos, extra, es_yogur)

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

if len(yogures) >= 2:
    print("\nComparación de grupo calórico entre el primer y segundo producto:")
    if yogures[0] == yogures[1]:
        print("Pertenecen al mismo grupo calórico (mismas calorías para 100 ml).")
    else:
        print("NO pertenecen al mismo grupo calórico.")
