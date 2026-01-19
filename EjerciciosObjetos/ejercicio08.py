from abc import ABC, abstractmethod
import math


class Figura(ABC):
    """Clase base abstracta para figuras geométricas"""
    
    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """Calcula el perímetro de la figura"""
        pass
    
    @abstractmethod
    def aplicar_escala(self, factor):
        """Aplica un factor de escala a la figura"""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}"


class Rectangulo(Figura):
    """Clase para representar un rectángulo"""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def aplicar_escala(self, factor):
        self.base *= factor
        self.altura *= factor
    
    def __str__(self):
        return f"Rectángulo(base={self.base:.2f}, altura={self.altura:.2f})"


class Circulo(Figura):
    """Clase para representar un círculo"""
    
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def aplicar_escala(self, factor):
        self.radio *= factor
    
    def __str__(self):
        return f"Círculo(radio={self.radio:.2f})"


class Triangulo(Figura):
    """Clase para representar un triángulo"""
    
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        # Fórmula de Herón
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def aplicar_escala(self, factor):
        self.lado1 *= factor
        self.lado2 *= factor
        self.lado3 *= factor
    
    def __str__(self):
        return f"Triángulo(lados={self.lado1:.2f}, {self.lado2:.2f}, {self.lado3:.2f})"


def calcular_area_total(figuras):
    """Calcula la suma de las áreas de todas las figuras"""
    return sum(figura.calcular_area() for figura in figuras)


def calcular_perimetro_total(figuras):
    """Calcula la suma de los perímetros de todas las figuras"""
    return sum(figura.calcular_perimetro() for figura in figuras)


def encontrar_mayor_triangulo(figuras):
    """Encuentra el triángulo con mayor área en la lista de figuras"""
    triangulos = [figura for figura in figuras if isinstance(figura, Triangulo)]
    
    if not triangulos:
        return None
    
    return max(triangulos, key=lambda t: t.calcular_area())


def mostrar_informacion_figuras(figuras):
    """Muestra información detallada de todas las figuras"""
    print("\n=== INFORMACIÓN DE FIGURAS ===")
    for i, figura in enumerate(figuras, 1):
        print(f"\nFigura {i}: {figura}")
        print(f"  Área: {figura.calcular_area():.2f}")
        print(f"  Perímetro: {figura.calcular_perimetro():.2f}")


def crear_figura_desde_input():
    """Solicita datos al usuario y crea una figura"""
    print("\nTipos de figuras disponibles:")
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo")
    
    while True:
        try:
            opcion = int(input("\nSelecciona el tipo de figura (1-3): "))
            if opcion not in [1, 2, 3]:
                print("Opción no válida. Introduce 1, 2 o 3.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    try:
        if opcion == 1:
            base = float(input("Introduce la base del rectángulo: "))
            altura = float(input("Introduce la altura del rectángulo: "))
            return Rectangulo(base, altura)
        
        elif opcion == 2:
            radio = float(input("Introduce el radio del círculo: "))
            return Circulo(radio)
        
        elif opcion == 3:
            lado1 = float(input("Introduce el primer lado del triángulo: "))
            lado2 = float(input("Introduce el segundo lado del triángulo: "))
            lado3 = float(input("Introduce el tercer lado del triángulo: "))
            return Triangulo(lado1, lado2, lado3)
    
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
        return None


# Programa principal
if __name__ == "__main__":
    print("=== APLICACIÓN DE DIBUJO - GESTOR DE FIGURAS ===")
    
    # Solicitar número de figuras
    while True:
        try:
            num_figuras = int(input("\n¿Cuántas figuras deseas crear? "))
            if num_figuras <= 0:
                print("Debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    # Crear lista de figuras
    figuras = []
    for i in range(num_figuras):
        print(f"\n--- Figura {i + 1} de {num_figuras} ---")
        figura = crear_figura_desde_input()
        if figura:
            figuras.append(figura)
            print(f"✓ {figura} creado correctamente.")
        else:
            print("Error al crear la figura. Intenta de nuevo.")
            i -= 1  # Repetir esta iteración
    
    if not figuras:
        print("\nNo se crearon figuras. Programa finalizado.")
        exit()
    
    # Mostrar información de todas las figuras
    mostrar_informacion_figuras(figuras)
    
    # Calcular y mostrar área total
    area_total = calcular_area_total(figuras)
    print(f"\n=== ESTADÍSTICAS GLOBALES ===")
    print(f"Área total de todas las figuras: {area_total:.2f}")
    
    # Calcular y mostrar perímetro total
    perimetro_total = calcular_perimetro_total(figuras)
    print(f"Perímetro total de todas las figuras: {perimetro_total:.2f}")
    
    # Encontrar el mayor triángulo
    mayor_triangulo = encontrar_mayor_triangulo(figuras)
    if mayor_triangulo:
        print(f"\n=== MAYOR TRIÁNGULO ===")
        print(f"{mayor_triangulo}")
        print(f"Área: {mayor_triangulo.calcular_area():.2f}")
        print(f"Perímetro: {mayor_triangulo.calcular_perimetro():.2f}")
    
    # Demostración de escalado
    print("\n=== DEMOSTRACIÓN DE ESCALADO ===")
    escalar = input("\n¿Deseas escalar alguna figura? (s/n): ").lower()
    if escalar == 's':
        print(f"\nFiguras disponibles:")
        for i, figura in enumerate(figuras, 1):
            print(f"{i}. {figura}")
        
        try:
            indice = int(input("\n¿Qué figura deseas escalar? (número): ")) - 1
            if 0 <= indice < len(figuras):
                factor = float(input("¿Qué factor de escala aplicar? "))
                print(f"\nAntes del escalado:")
                print(f"{figuras[indice]}")
                print(f"Área: {figuras[indice].calcular_area():.2f}")
                
                figuras[indice].aplicar_escala(factor)
                
                print(f"\nDespués de aplicar escala x{factor}:")
                print(f"{figuras[indice]}")
                print(f"Área: {figuras[indice].calcular_area():.2f}")
            else:
                print("Índice no válido.")
        except (ValueError, IndexError):
            print("Error en la entrada de datos.")
    
    # Contar tipos de figuras
    print("\n=== DISTRIBUCIÓN DE FIGURAS ===")
    num_rectangulos = sum(1 for f in figuras if isinstance(f, Rectangulo))
    num_circulos = sum(1 for f in figuras if isinstance(f, Circulo))
    num_triangulos = sum(1 for f in figuras if isinstance(f, Triangulo))
    
    print(f"Rectángulos: {num_rectangulos}")
    print(f"Círculos: {num_circulos}")
    print(f"Triángulos: {num_triangulos}")
    print(f"Total de figuras: {len(figuras)}")