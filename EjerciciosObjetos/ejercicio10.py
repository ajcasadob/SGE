# Simula en un programa con varias clases y herencia (no tiene que ser múltiple), la gestión de pedidos a una
#empresa. Debe existir distintos tipos de pedidos y los métodos reescritos deben calcular el precio final de los
#distintos pedidos. Por otro lado, debe existir alguna clase donde haya métodos que hagan cálculos estadísticos
#sobre los pedidos (por ejemplo, la medida de los pedidos, media de distancia a la que se mandan, búsquedas
#de varios tipos, etc.).


class Pedido:
    
    def __init__(self,precioBase:float,cant:int,nombre:str):
        self.precioBase = precioBase
        self.cant = cant
        self.nombre = nombre
        
    def calcular_precio(self):
        return self.precioBase * self.cant
    
    def __str__(self):
        return f'{self.nombre},{self.precioBase},{self.cant}'
    
    
    

class Hamburguesa(Pedido):
    
    
    def __init__(self, precioBase, cant,nombre):
        super().__init__(precioBase, cant,nombre)
        
        
    def calcular_precio(self):
        if self.cant <= 2:
            raise ErrorCantidad('La cantidad debe de ser superior a 2')
        return super().calcular_precio()
    

class Pizza(Pedido):
    
    def __init__(self, precioBase, cant, nombre,tam:str):
        super().__init__(precioBase, cant, nombre)
        self.tam = tam
        
        
    def calcular_precio(self):
        
        if self.tam == 'grande':
            return super().calcular_precio()+10
        elif self.tam == 'mediana':
            return super().calcular_precio()+5
        
        return super().calcular_precio()
    
    
    
class ErrorCantidad(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        
        
class Principal:
    
    pizza1= Pizza(14,2,'4 quesos','grande')
    hamburguesa1= Hamburguesa(18,1,'la abuela')
    
    listaPedidos = []
    
    listaPedidos.append(pizza1, hamburguesa1)
    
    for i in listaPedidos:
        print(i)