class Droid:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    def mover(self, distancia):
        print(f"{self.nombre} se mueve {distancia} metros (movimiento genérico).")

    def atacar(self, enemigos):
        print(f"{self.nombre} ataca a {enemigos} enemigos (ataque genérico).")


class DroidTerrestre(Droid):
    def __init__(self, nombre, energia, velocidad):
        super().__init__(nombre, energia)
        self.velocidad = velocidad  # m/s

    def mover(self, distancia):
        tiempo = distancia / self.velocidad
        print(f"{self.nombre} avanza {distancia} m por tierra en {tiempo:.2f} s.")


class DroidAereo(Droid):
    def __init__(self, nombre, energia, altitud_maxima):
        super().__init__(nombre, energia)
        self.altitud_maxima = altitud_maxima  # m

    def mover(self, distancia):
        energia_gastada = distancia * 2
        self.energia -= energia_gastada
        print(f"{self.nombre} vuela {distancia} m y gasta {energia_gastada} de energía. "
            f"Energía restante: {self.energia}.")


class DroidAsalto(DroidTerrestre, DroidAereo):
    def __init__(self, nombre, energia, velocidad, altitud_maxima, danio_base):
        Droid.__init__(self, nombre, energia)
        self.velocidad = velocidad
        self.altitud_maxima = altitud_maxima
        self.danio_base = danio_base

    def mover(self, distancia):
        tiempo = distancia / self.velocidad
        energia_gastada = distancia * 2
        self.energia -= energia_gastada

        print(f"{self.nombre} de asalto recorre {distancia} m.")
        print(f"  - Tiempo (modo terrestre): {tiempo:.2f} s")
        print(f"  - Energía gastada (modo aéreo): {energia_gastada}")
        print(f"  - Energía restante: {self.energia}")

    def atacar(self, enemigos):
        danio_total = self.danio_base * enemigos
        print(f"{self.nombre} elimina a {enemigos} enemigos.")
        print(f"  - Daño base: {self.danio_base}")
        print(f"  - Daño total infligido: {danio_total}")



d1 = DroidAsalto("R-77", energia=1000, velocidad=10, altitud_maxima=500, danio_base=50)

d1.mover(100)      
d1.atacar(8)       
print(f"Energía final de {d1.nombre}: {d1.energia}")
