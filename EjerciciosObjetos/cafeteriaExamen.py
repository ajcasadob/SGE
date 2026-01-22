class Beverage:
    
    def __init__(self,nombre:str,cost:float):
        self.nombre = nombre
        self._cost=cost

    @property
    def getCost (self):
        return self._cost
    
    @getCost.setter
    def cost(self,coste:float):
        self._coste=coste
    
class PremiumIngredients(Beverage):
    
    def __init__(self, nombre, cost,listIngredientes:list[str]):
        super().__init__(nombre, cost)
        self.listIngredientes = listIngredientes
        
    @staticmethod
    def get_available_extras()->tuple:
        disponinle =("Caramelo","Canela","Chocolate","Nata")
        return disponinle
    
class CafeService(Beverage):
    
    def __init__(self, nombre, cost,temperatura:tuple,points:int):
        Beverage.__init__(self,nombre, cost)
        self.temperatura = temperatura
        self.points = points
    
    @staticmethod
    def get_service_hours():
        return "Horario: 7:00 - 22:00"

class SpecialCoffe(PremiumIngredients,CafeService):
    total_order =0
    
    def __init__(self, nombre, cost, listIngredientes,temperatura:tuple,points:int):
        PremiumIngredients.__init__(self,nombre, cost, listIngredientes)
        CafeService.__init__(self,nombre,cost,temperatura,points)
        
        
    @classmethod
    def show_statistics (cls):
        return (f'Total de cafés especiales pedidos: {cls.totalOrder}')
    
    def __str__(self):
        return f'{self.nombre},{self._cost},{self.listIngredientes},{self.temperatura},{self.points}'
    

class Principal:
    
    cafe1= SpecialCoffe("Solo",2.0,["Nata"],("caliente"),2)
    cafe2=SpecialCoffe("Cafe largo",4.0,["Leche"],("Frio"),5)
    cafe3= SpecialCoffe("Cafe especial",5.0,["Frio"],("Frioote",6))
    
    SpecialCoffe.show_statistics()
    Cafes: list[Beverage] 
    listaCafe =[]
    listaCafe.append(cafe1)
    listaCafe.append(cafe2)
    listaCafe.append(cafe3)