# La Martingala es una estrategia de apuestas que se popularizó en la ruleta y tiene la siguiente estructura
# (usaremos radom):
# • 🎲 Se comienza con una apuesta inicial. Se apuesta siempre al ⚫.
# • ⚫ Si se gana, se vuelve a la apuesta inicial.
# • 🔴 Si se pierde, se dobla la apuesta.
# La esencia de esta estrategia es que cuando perdemos, doblamos la siguiente apuesta para intentar recuperar la
# cantidad perdida. En la teoría, suena bien.
# Intenta crear una función que simule esta estrategia, definiendo una cantidad inicial, una apuesta, una
# probabilidad de ganar y una cantidad objetivo a ganar, después de la cual se debe para la simulación.
# Puedes intentar buscar una estrategia que reduzca el riesgo de bancarrota.

import random


def simular_martingala(dinero_inicial, apuesta_inicial, probabilidad_ganar, objetivo, limite_apuesta_max=None):
    dinero = dinero_inicial
    apuesta_actual = apuesta_inicial
    ronda = 0
    
   
    if limite_apuesta_max is None:
        limite_apuesta_max = dinero_inicial * 0.25
    
    while dinero > 0 and dinero < objetivo:
        ronda += 1
        
       
        if apuesta_actual > dinero:
            apuesta_actual = dinero
        
        
        if apuesta_actual > limite_apuesta_max:
            apuesta_actual = limite_apuesta_max
        
        
        gana = random.random() < probabilidad_ganar
        
        if gana:
            dinero += apuesta_actual
            apuesta_actual = apuesta_inicial
        else:
            dinero -= apuesta_actual
            apuesta_actual *= 2
    
    return {
        'exito': dinero >= objetivo,
        'dinero_final': dinero,
        'rondas': ronda,
        'ganancia': dinero - dinero_inicial
    }


print("SIMULADOR DE ESTRATEGIA MARTINGALA")
print("=" * 50)

dinero_inicial = float(input("Dinero inicial: "))
apuesta_inicial = float(input("Apuesta inicial: "))
probabilidad_ganar = float(input("Probabilidad de ganar (0-1): "))
objetivo = float(input("Objetivo a alcanzar: "))

usar_limite = input("¿Usar límite máximo de apuesta? (s/n): ").lower()
if usar_limite == 's':
    limite_apuesta_max = float(input("Límite máximo de apuesta: "))
else:
    limite_apuesta_max = None

print("\n" + "=" * 50)
print("INICIANDO SIMULACIÓN...")
print("=" * 50 + "\n")

resultado = simular_martingala(dinero_inicial, apuesta_inicial, probabilidad_ganar, objetivo, limite_apuesta_max)

print("\n" + "=" * 50)
print("RESULTADOS DE LA SIMULACIÓN")
print("=" * 50)

if resultado['exito']:
    print("¡OBJETIVO ALCANZADO!")
else:
    print("BANCARROTA")

print(f"\nDinero final: {resultado['dinero_final']:.2f}€")
print(f"Rondas jugadas: {resultado['rondas']}")
print(f"Ganancia/Pérdida: {resultado['ganancia']:+.2f}€")
print(f"Rentabilidad: {(resultado['ganancia']/dinero_inicial)*100:+.2f}%")
print("=" * 50)
