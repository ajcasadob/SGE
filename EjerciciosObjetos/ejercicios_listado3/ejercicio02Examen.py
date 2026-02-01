class Animales:
    def __init__(self, nombre: str, coste: float):
        self.nombre = nombre
        self.coste = coste  
    
    def calcularCoste(self, numDiasAnio: int) -> float:
        return self.coste * numDiasAnio


class Osos(Animales):
    def __init__(self, nombre, coste: float, precioCarnePescado: float):
        super().__init__(nombre, coste)
        self.precioCarnePescado = precioCarnePescado
    
    def calcularCoste(self, numDiasAnio):
        semanasAnio = 52
        coste_carne = self.precioCarnePescado * 2 * semanasAnio  
        return coste_carne + super().calcularCoste(numDiasAnio)


class Serpientes(Animales):
    def __init__(self, nombre: str, coste: float, numInsectos: int, precioInsecto: float):
        super().__init__(nombre, coste)
        self.numInsectos = numInsectos  
        self.precioInsecto = precioInsecto
    
    def calcularCoste(self, numDiasAnio):
        semanasAnio = 52
        coste_insectos = self.numInsectos * self.precioInsecto * 2 * semanasAnio  
        return coste_insectos + super().calcularCoste(numDiasAnio)


class Zoo:
    DIAS_ANIO = 365
    
    @staticmethod
    def coste_total(animales: list, cantidades: list[int]) -> float:
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







oso_panda = Osos("Panda", 15.0, 25.0)
oso_grizzly = Osos("Grizzly", 20.0, 30.0)
serpiente_rey = Serpientes("Serpiente Rey", 5.0, 50, 0.2) 
serpiente_piton = Serpientes("Piton", 8.0, 80, 0.15)
leon = Animales("León", 45.0)

print("\nAnimales disponibles:")
print(f"1. {oso_panda.nombre}: {oso_panda.coste}€/día + carne especial")
print(f"2. {oso_grizzly.nombre}: {oso_grizzly.coste}€/día + carne especial") 
print(f"3. {serpiente_rey.nombre}: {serpiente_rey.coste}€/día + insectos")
print(f"4. {serpiente_piton.nombre}: {serpiente_piton.coste}€/día + insectos")
print(f"5. {leon.nombre}: {leon.coste}€/día (normal)")


num_tipos = int(input("\n¿Cuántos tipos de animales quieres incluir? "))
animales_lista = []
cantidades = []

for i in range(num_tipos):
    print(f"\n--- Tipo {i+1} ---")
    if i == 0:
        animal = oso_panda
    elif i == 1:
        animal = oso_grizzly
    elif i == 2:
        animal = serpiente_rey
    elif i == 3:
        animal = serpiente_piton
    else:
        animal = leon
    
    cantidad = int(input(f"¿Cuántos {animal.nombre}? "))
    animales_lista.append(animal)
    cantidades.append(cantidad)


coste_total = Zoo.coste_total(animales_lista, cantidades)
print(f"\nCoste total anual del zoo: {coste_total:.2f} €")


umbral = float(input("Umbral para descuento (€): "))
porcentaje_desc = float(input("Porcentaje descuento (%): "))
descuento = Zoo.calcular_descuento(coste_total, umbral, porcentaje_desc)
print(f"Descuento aplicado: {descuento:.2f} €")
print(f"Coste final con descuento: {coste_total - descuento:.2f} €")


osos_lista = []
cant_osos = []
for i in range(len(animales_lista)):
    if isinstance(animales_lista[i], Osos):
        osos_lista.append(animales_lista[i])
        cant_osos.append(cantidades[i])

coste_osos = Zoo.coste_solo_osos(osos_lista, cant_osos)
print(f"\nCoste solo en osos: {coste_osos:.2f} € ({coste_osos/coste_total*100:.1f}% del total)")
