

class ErrorPedido(Exception):
    
    pass


class DatosInvalidosError(ErrorPedido):
    
    pass


class ListaVaciaError(ErrorPedido):
    
    pass




class Pedido:
    def __init__(self, id_pedido, cliente, importe_base, distancia_km):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.importe_base = importe_base
        self.distancia_km = distancia_km


    def calcular_precio_final(self):
        return self.importe_base


    def __str__(self):
        return f"Pedido {self.id_pedido} de {self.cliente}"



class PedidoNormal(Pedido):
    def __init__(self, id_pedido, cliente, importe_base, distancia_km, iva=0.21):
        super().__init__(id_pedido, cliente, importe_base, distancia_km)
        self.iva = iva


    def calcular_precio_final(self):
        if self.importe_base <= 0:
            raise DatosInvalidosError(f"El importe base debe ser mayor que 0. Recibido: {self.importe_base}")
        return self.importe_base * (1 + self.iva)



class PedidoUrgente(Pedido):
    def __init__(self, id_pedido, cliente, importe_base, distancia_km, recargo_urgente=10.0, recargo_km=0.5):
        super().__init__(id_pedido, cliente, importe_base, distancia_km)
        self.recargo_urgente = recargo_urgente
        self.recargo_km = recargo_km


    def calcular_precio_final(self):
        if self.distancia_km < 0:
            raise DatosInvalidosError(f"La distancia no puede ser negativa. Recibida: {self.distancia_km} km")
        return self.importe_base + self.recargo_urgente + self.distancia_km * self.recargo_km



class PedidoInternacional(Pedido):
    def __init__(self, id_pedido, cliente, importe_base, distancia_km, tasa_aduanas=0.15, tipo_cambio=1.1):
        super().__init__(id_pedido, cliente, importe_base, distancia_km)
        self.tasa_aduanas = tasa_aduanas
        self.tipo_cambio = tipo_cambio


    def calcular_precio_final(self):
        subtotal = self.importe_base * (1 + self.tasa_aduanas)
        return subtotal * self.tipo_cambio



class EstadisticasPedidos:
    def __init__(self, pedidos):
        self.pedidos = pedidos


    def media_importe_base(self):
        if len(self.pedidos) == 0:
            return 0
        suma = 0
        for p in self.pedidos:
            suma = suma + p.importe_base
        return suma / len(self.pedidos)


    def media_precio_final(self):
        if len(self.pedidos) == 0:
            raise ListaVaciaError("No se puede calcular la media del precio final sin pedidos")
        suma = 0
        for p in self.pedidos:
            suma = suma + p.calcular_precio_final()
        return suma / len(self.pedidos)


    def media_distancia(self):
        if len(self.pedidos) == 0:
            return 0
        suma = 0
        for p in self.pedidos:
            suma = suma + p.distancia_km
        return suma / len(self.pedidos)


    def pedidos_mayores_que(self, cantidad):
        resultado = []
        for p in self.pedidos:
            if p.calcular_precio_final() > cantidad:
                resultado.append(p)
        return resultado


    def buscar_por_cliente(self, nombre_cliente):
        resultado = []
        for p in self.pedidos:
            if p.cliente == nombre_cliente:
                resultado.append(p)
        return resultado





p1 = PedidoNormal(1, "Alice", 100.0, 50)
p2 = PedidoUrgente(2, "Bob", 80.0, 20)
p3 = PedidoInternacional(3, "Alice", 200.0, 800)
p4 = PedidoNormal(4, "Carlos", 50.0, 10)


pedidos = [p1, p2, p3, p4]


print("PRECIOS FINALES:")
for pedido in pedidos:
    print(pedido, "->", pedido.calcular_precio_final())


estadisticas = EstadisticasPedidos(pedidos)


print("\nESTADÍSTICAS:")
print("Media importe base:", estadisticas.media_importe_base())
print("Media precio final:", estadisticas.media_precio_final())
print("Media distancia:", estadisticas.media_distancia())


print("\nPedidos con precio final > 150:")
pedidos_caros = estadisticas.pedidos_mayores_que(150)
for pedido in pedidos_caros:
    print(pedido, "->", pedido.calcular_precio_final())


print("\nPedidos del cliente 'Alice':")
pedidos_alice = estadisticas.buscar_por_cliente("Alice")
for pedido in pedidos_alice:
    print(pedido, "->", pedido.calcular_precio_final())





print("EJEMPLOS DE MANEJO DE EXCEPCIONES")



print("\n1. Pedido Normal con importe negativo:")
try:
    p_invalido = PedidoNormal(5, "David", -50.0, 10)
    precio = p_invalido.calcular_precio_final()
except DatosInvalidosError as e:
    print(f" {e}")


print("\n2. Pedido Urgente con distancia negativa:")
try:
    p_invalido2 = PedidoUrgente(6, "Eva", 100.0, -20)
    precio = p_invalido2.calcular_precio_final()
except DatosInvalidosError as e:
    print(f" {e}")

print("\n3. Estadísticas con lista vacía:")
try:
    estadisticas_vacias = EstadisticasPedidos([])
    media = estadisticas_vacias.media_precio_final()
except ListaVaciaError as e:
    print(f" {e}")
