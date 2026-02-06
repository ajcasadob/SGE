from modelo.animales import Animales



class Zoo:
    DIAS_ANIO = 365
    
    @staticmethod
    def coste_total(animales: list[Animales], cantidades: list[int]) -> float:
        total = 0.0
        for i in range(len(animales)):
            coste_animal = animales[i].calcularCoste(Zoo.DIAS_ANIO)
            total = total + (coste_animal * cantidades[i])
        return total
    
    @staticmethod
    def calcular_descuento(total_gasto: float, umbral_descuento: float, porcentaje_descuento: float) -> float:
        if total_gasto > umbral_descuento:
            descuento = total_gasto * porcentaje_descuento / 100
            return descuento
        return 0.0
    
    @staticmethod
    def coste_solo_osos(osos: list[Osos], cantidades: list[int]) -> float:
        total_osos = 0.0
        for i in range(len(osos)):
            coste_oso = osos[i].calcularCoste(Zoo.DIAS_ANIO)
            total_osos = total_osos + (coste_oso * cantidades[i])
        return total_osos
