from __future__ import annotations

class StarWarsDroid:
    pass
c3po = StarWarsDroid()
r2d2 = StarWarsDroid()
bb8 = StarWarsDroid()    




##Metodo decorador, con esto conseguimos cambiar la funcion del metodo sin alterar su codigo
class Droid:
    @staticmethod
    def audit (method):
        def wrapper (self, *args, **kwargs):
            print(f'Droid {self.name} running {method.__name__}')
            return method(self, *args, **kwargs)
        return wrapper
    
    def __init__(self, name: str):
        self.name = name
        self.pos = [0,0]
        
    @audit
    def move (self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y
    
    @audit
    def reset (self):
        self.pos = [0,0]
##El decorador se puede poner dentro o fuera de la clase, por una cuestion de encapsulamiento 
# tendria sentido dejarlo dentro de la clase como metodo estatico.


##METODOS MAGICOS

##Los metodos magicos se disparan de manera transparente cuando utilizamos ciertas estructuras y expresiones del lenguaje.

## A continucion muestro una equivalencia  entre operadores y metodos magicos
## __eq__ es lo mismo que ==

class Droid:
    def __init__ ( self, name: str, serial_number: int):
        self.name = name
        self.serial_number= serial_number
        
    def __eq__(self, droid: Droid)-> bool:
        return self.name == droid.name
    
    
    droid1 = Droid('C-3PO')
    droid2 = Droid('C-3PO')
    
    print(droid1 == droid2)
    
    droid1 = Droid('C-3P4')
    droid2 = Droid('C-3PO')
    
    droid1.__eq__(droid2)
    
##Existen muchos otros en la documentacion oficial de Pyhton

##Veamos un ejemplo donde sumamos dos droides

class Droid:
    
    def __init__(self, name: str, power:int):
        self.name = name
        self.power = power
        
    def __ad__(self, other: Droid)-> Droid:
        new_name = self.name + '-' + other.name
        new_power = self.power + other.power
        return Droid(new_name, new_power)
    
    

## __eq__ seria lo mismo que ==
# __ne__ seria lo mismo que !=
# __lt__ seria lo mismo que <
# __le__ seria lo mismo que <=
# __gt__ seria lo mismo que >
# __ge__ seria lo mismo que >=
# __add__ seria lo mismo que +
# __sub__ seria lo mismo que -
# __mul__ seria lo mismo que *
# __truediv__ seria lo mismo que /
# __floordiv__ seria lo mismo que //
# __mod__ seria lo mismo que %
# __pow__ seria lo mismo que **

#SOBRECARGA DE OPERADORES

#La sobrecarga de operadores es una característica que permite cambiar el comportamiento de los
# operadores estándar (+, -, *, etc.) para que funcionen con tus propias clases. En Python, esto se
# logra definiendo métodos especiales que comienzan y terminan con doble guión bajo (__).

#El ejemplo del Droid muestra cómo el método __add__ puede aceptar múltiples tipos de argumentos y comportarse de forma diferente según el tipo.
class Droid:
    """
    Representa un droide con nombre y nivel de energía.
    Demuestra sobrecarga de operadores con múltiples tipos.
    """
    
    def __init__(self, name: str, power: int):
        """
        Constructor del droide.
        
        Args:
            name: Nombre del droide
            power: Nivel de energía inicial
        """
        self.name = name
        self.power = power
    
    def __add__(self, other: Droid | int) -> Droid:
        """
        Sobrecarga del operador + (suma).
        
        Comportamiento según el tipo:
        - Droid + Droid: Fusiona dos droides (suma nombres y energías)
        - Droid + int: Aumenta la energía del droide
        
        Args:
            other: Otro droide o un número entero
            
        Returns:
            Nuevo objeto Droid resultante de la operación
            
        Raises:
            TypeError: Si other no es Droid ni int
        """
        # CASO 1: Si sumamos dos droides
        if isinstance(other, Droid):
            # Concatenar nombres con guión
            new_name = self.name + "-" + other.name
            # Sumar las energías de ambos droides
            new_power = self.power + other.power
        
        # CASO 2: Si sumamos un número entero
        elif isinstance(other, int):
            # Mantener el mismo nombre
            new_name = self.name
            # Aumentar la energía en el valor del entero
            new_power = self.power + other
        
        else:
            # Si no es ninguno de los tipos esperados, error
            return NotImplemented
        
        # Crear y devolver un nuevo droide con los valores calculados
        return Droid(new_name, new_power)
    
    def __str__(self) -> str:
        """Representación legible del droide"""
        return f"Droid({self.name}, power={self.power})"

##El método __str__ es uno de los métodos mágicos más utilizados en Python y permite definir cómo se representa un objeto
# como cadena de texto. Este método se invoca automáticamente cuando usas print(), str() o interpolación de strings con f-strings.
"""
================================================================================
MÉTODOS MÁGICOS: __str__ vs __repr__
================================================================================

Diferencias clave:
- __str__: Representación INFORMAL para USUARIOS (legible y amigable)
- __repr__: Representación OFICIAL para DESARROLLADORES (técnica y completa)

Cuándo se invocan:
- __str__: Con print(), str(), f-strings
- __repr__: En el intérprete interactivo, repr(), o como fallback si no hay __str__
"""


class Droid:
    """
    Clase que demuestra la diferencia entre __str__ y __repr__.
    Representa un droide con nombre y número de serie.
    """
    
    def __init__(self, name: str, serial_number: int = 0):
        """
        Constructor del droide.
        
        Args:
            name: Nombre del droide
            serial_number: Número de serie (opcional)
        """
        self.name = name
        self.serial_number = serial_number
    
    def __str__(self):
        """
        MÉTODO MÁGICO: __str__
        
        PROPÓSITO:
        Proporciona una representación LEGIBLE y AMIGABLE del objeto
        orientada a usuarios finales.
        
        CUÁNDO SE INVOCA:
        1. print(objeto)         → Llamada implícita
        2. str(objeto)           → Llamada explícita
        3. f"{objeto}"           → En f-strings/interpolación
        
        CARACTERÍSTICAS:
        - Debe retornar un string (str)
        - Diseñado para ser LEGIBLE por humanos
        - Puede omitir detalles técnicos
        - NO necesita permitir recrear el objeto
        - Enfocado en CLARIDAD para el usuario
        
        EJEMPLO DE USO:
        >>> droid = Droid("C-3PO", 123456)
        >>> print(droid)
        Hi there! I'm C-3PO
        
        Returns:
            str: Mensaje amigable y descriptivo
        """
        return f"Hi there! I'm {self.name}"
    
    def __repr__(self):
        """
        MÉTODO MÁGICO: __repr__
        
        PROPÓSITO:
        Proporciona una representación TÉCNICA y COMPLETA del objeto
        orientada a desarrolladores y debugging.
        
        CUÁNDO SE INVOCA:
        1. repr(objeto)           → Llamada explícita
        2. objeto (en intérprete) → Al escribir solo el nombre del objeto
        3. print(objeto)          → SI NO existe __str__ (fallback)
        
        CARACTERÍSTICAS:
        - Debe retornar un string (str)
        - Diseñado para ser INEQUÍVOCO y COMPLETO
        - Idealmente debe permitir RECREAR el objeto:
        eval(repr(obj)) == obj
        - Útil para logging y debugging
        - Puede incluir info técnica (direcciones de memoria, tipos, etc.)
        
        FORMATO TÍPICO RECOMENDADO:
        NombreClase(param1=valor1, param2=valor2)
        
        EJEMPLO DE USO:
        >>> droid = Droid("C-3PO", 123456)
        >>> repr(droid)
        [Droid] C-3PO @ 0x103e4e350
        >>> droid  # En el intérprete interactivo
        [Droid] C-3PO @ 0x103e4e350
        
        Returns:
            str: Representación técnica completa
            
        Nota:
            hex(id(self)) → Obtiene la dirección de memoria del objeto
                        en formato hexadecimal.
            Útil para identificar objetos únicos durante debugging.
        """
        # Incluimos el nombre, número de serie y dirección de memoria
        return f"[Droid] {self.name} serial-no {self.serial_number} @ {hex(id(self))}"

"""
================================================================================
📚 RESUMEN DE DIFERENCIAS
================================================================================

┌─────────────┬──────────────────────────┬──────────────────────────┐
│             │         __str__          │         __repr__         │
├─────────────┼──────────────────────────┼──────────────────────────┤
│ Audiencia   │ Usuarios finales         │ Desarrolladores          │
│ Propósito   │ Legible y amigable       │ Técnico y completo       │
│ Estilo      │ Informal                 │ Formal                   │
│ Objetivo    │ Claridad                 │ Precisión                │
│ Invocación  │ print(), str(), f-string │ repr(), intérprete       │
│ Fallback    │ Usa __repr__ si no existe│ Representación por defecto│
│ Debe recrear│ No necesario             │ Idealmente sí            │
│ Info técnica│ Puede omitir             │ Debe incluir             │
└─────────────┴──────────────────────────┴──────────────────────────┘


✅ BUENAS PRÁCTICAS:

1. SIEMPRE implementa __repr__ (mínimo indispensable)
2. Implementa __str__ solo si necesitas versión simplificada
3. __repr__ debe permitir identificar el objeto inequívocamente
4. __str__ debe ser corto y descriptivo
5. Ambos DEBEN retornar string (str)


🎯 REGLA DE ORO:
"__repr__ es para desarrolladores, __str__ es para usuarios"


📝 EJEMPLO DE IMPLEMENTACIÓN TÍPICA:

def __str__(self):
    return f"{self.name} - {self.price}€"

def __repr__(self):
    return f"Producto(name='{self.name}', price={self.price}, stock={self.stock})"

================================================================================
"""
"""
================================================================================
GESTORES DE CONTEXTO: __enter__ y __exit__
================================================================================

Un gestor de contexto permite ejecutar código automáticamente:
- Al ENTRAR a un bloque: __enter__()
- Al SALIR de un bloque: __exit__()

Se usan con la sentencia 'with' para garantizar limpieza de recursos.

Casos de uso típicos:
- Abrir/cerrar archivos
- Medir tiempos de ejecución
- Adquirir/liberar locks
- Conectar/desconectar bases de datos
- Iniciar/finalizar transacciones
"""

from time import time


class Timer:
    """
    Gestor de contexto para medir tiempos de ejecución.
    Ejemplo básico de __enter__ y __exit__.
    """
    
    def __enter__(self):
        """
        MÉTODO MÁGICO: __enter__
        
        CUÁNDO SE EJECUTA:
        Al entrar al bloque 'with', ANTES de ejecutar el código interno.
        
        PROPÓSITO:
        Realizar acciones de INICIALIZACIÓN o PREPARACIÓN.
        
        SINTAXIS:
        with Timer() as timer:
            # Aquí ya se ejecutó __enter__
            pass
        
        CARACTERÍSTICAS:
        - Se ejecuta automáticamente al usar 'with'
        - Puede retornar un valor que se asigna a la variable 'as'
        - Si retorna self, podemos acceder al gestor
        - Si no retorna nada, 'as' será None
        
        Returns:
            Opcionalmente retorna un objeto (típicamente self)
            que se asigna a la variable después de 'as'
        """
        # Guardar el tiempo de inicio
        self.start = time()
        print("⏱️  Timer iniciado...")
        # Retornar self permite acceder al timer si es necesario
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        MÉTODO MÁGICO: __exit__
        
        CUÁNDO SE EJECUTA:
        Al salir del bloque 'with', DESPUÉS de ejecutar el código interno.
        Se ejecuta SIEMPRE, incluso si hay errores.
        
        PROPÓSITO:
        Realizar acciones de LIMPIEZA o FINALIZACIÓN.
        
        PARÁMETROS (para manejo de excepciones):
        - exc_type: Tipo de excepción si ocurrió (ej: ValueError, None si no hubo)
        - exc_value: Instancia de la excepción con el mensaje
        - exc_traceback: Objeto traceback con la pila de llamadas
        
        Si NO hubo excepciones: los 3 parámetros son None
        Si HUBO excepción: contienen información del error
        
        RETORNO:
        - True: Suprime la excepción (no se propaga)
        - False o None: La excepción se propaga normalmente
        
        CARACTERÍSTICAS:
        - Se ejecuta SIEMPRE, incluso con errores
        - Garantiza limpieza de recursos
        - Puede manejar excepciones del bloque
        
        Args:
            exc_type: Tipo de la excepción (o None)
            exc_value: Valor/mensaje de la excepción (o None)
            exc_traceback: Traceback de la excepción (o None)
        
        Returns:
            bool: True para suprimir excepción, False/None para propagarla
        """
        # Calcular tiempo transcurrido
        self.end = time()
        exec_time = self.end - self.start
        
        print(f"⏱️  Execution time (seconds): {exec_time:.5f}")
        
        # Manejar excepciones si es necesario
        if exc_type is not None:
            print(f"⚠️  Se produjo un error: {exc_type.__name__}: {exc_value}")
            # Retornar False permite que la excepción se propague
            return False
        
        # No retornamos nada (None) = la excepción se propaga si existe


class Droid:
    """
    Clase Droid para demostrar gestores de contexto.
    """
    
    def __init__(self, name: str):
        """
        Constructor del droide.
        
        Args:
            name: Nombre del droide
        """
        self.name = name
        self.covered_distance = 0
    
    def move_up(self, steps: int) -> None:
        """
        Mueve el droide una cantidad de pasos.
        
        Args:
            steps: Número de pasos a mover
        """
        self.covered_distance += steps
        print(f"🚶 Moving {steps} steps")


class FrozenDroid:
    """
    GESTOR DE CONTEXTO para droides.
    
    Crea un droide temporalmente y resetea su distancia al salir.
    Demuestra uso práctico de __enter__ y __exit__.
    """
    
    def __enter__(self):
        """
        Se ejecuta al entrar al bloque 'with'.
        
        ACCIONES:
        1. Crea un nuevo droide
        2. Lo retorna para usarlo en el bloque
        
        Returns:
            Droid: El droide creado para usar en el contexto
        """
        print("🧊 === ENTRANDO AL CONTEXTO: Droide congelado ===")
        self.droid = Droid("FrozenDroid")
        return self.droid  # Este objeto se asigna a 'as droid'
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Se ejecuta al salir del bloque 'with'.
        
        ACCIONES:
        1. Resetea la distancia recorrida
        2. Muestra estadísticas finales
        
        Args:
            exc_type: Tipo de excepción (None si no hubo)
            exc_value: Valor de excepción (None si no hubo)
            exc_traceback: Traceback (None si no hubo)
        
        Note:
            Usamos *err para capturar todos los parámetros de error
            sin necesidad de usarlos individualmente.
        """
        print(f"🧊 === SALIENDO DEL CONTEXTO: Reseteo activado ===")
        print(f"📊 Distancia antes de reseteo: {self.droid.covered_distance}")
        
        # Resetear distancia
        self.droid.covered_distance = 0
        
        print(f"📊 Distancia después de reseteo: {self.droid.covered_distance}")




"""
================================================================================
📚 RESUMEN: GESTORES DE CONTEXTO
================================================================================

SINTAXIS BÁSICA:
    with GestorContexto() as variable:
        # Código que se ejecuta en el contexto
        pass

FLUJO DE EJECUCIÓN:
    1. Se llama a __enter__()
    2. El valor retornado se asigna a 'variable' (si hay 'as')
    3. Se ejecuta el bloque de código indentado
    4. Se llama a __exit__() SIEMPRE (incluso con errores)

MÉTODOS REQUERIDOS:
    __enter__(self):
        - Inicialización/preparación
        - Retorna el objeto para usar (típicamente self)
    
    __exit__(self, exc_type, exc_value, exc_traceback):
        - Limpieza/finalización
        - Recibe info de excepciones si ocurrieron
        - Retorna True para suprimir excepción

PARÁMETROS DE __exit__:
    exc_type:      Clase de la excepción (ValueError, TypeError, etc.)
    exc_value:     Instancia con el mensaje de error
    exc_traceback: Información de la pila de llamadas
    
    Si NO hay error: los 3 son None

CASOS DE USO COMUNES:
    ✅ Archivos: open/close automático
    ✅ Conexiones BD: connect/disconnect
    ✅ Locks: acquire/release
    ✅ Transacciones: begin/commit/rollback
    ✅ Timers: start/stop
    ✅ Recursos temporales: create/cleanup

VENTAJAS:
    ✅ Garantiza limpieza incluso con errores
    ✅ Código más limpio y legible
    ✅ Evita olvidos de cerrar recursos
    ✅ Manejo consistente de recursos

EJEMPLO REAL (archivos):
    with open('archivo.txt', 'w') as f:
        f.write('Hola')
    # El archivo se cierra automáticamente

================================================================================
"""

    