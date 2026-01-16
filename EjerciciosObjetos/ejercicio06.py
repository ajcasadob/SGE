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
    """
    Simula la estrategia de apuestas Martingala.
    
    Args:
        dinero_inicial: Cantidad de dinero con la que se comienza
        apuesta_inicial: Apuesta inicial
        probabilidad_ganar: Probabilidad de ganar (ej: 18/37 ≈ 0.486 en ruleta europea)
        objetivo: Cantidad de dinero objetivo para detener la simulación
        limite_apuesta_max: Límite máximo de apuesta (para reducir riesgo de bancarrota)
    
    Returns:
        Diccionario con estadísticas de la simulación
    """
    dinero = dinero_inicial
    apuesta_actual = apuesta_inicial
    ronda = 0
    
    # Si no se especifica límite máximo, usar el 25% del dinero inicial
    # Esto ayuda a evitar la bancarrota rápida
    if limite_apuesta_max is None:
        limite_apuesta_max = dinero_inicial * 0.25
    
    while dinero > 0 and dinero < objetivo:
        ronda += 1
        
        # Verificar si tenemos suficiente dinero para la apuesta actual
        if apuesta_actual > dinero:
            apuesta_actual = dinero
        
        # Aplicar límite máximo de apuesta (estrategia de reducción de riesgo)
        if apuesta_actual > limite_apuesta_max:
            apuesta_actual = limite_apuesta_max
        
        # Simular la apuesta
        gana = random.random() < probabilidad_ganar
        
        if gana:
            # ⚫ Ganamos
            dinero += apuesta_actual
            # Resetear a apuesta inicial
            apuesta_actual = apuesta_inicial
        else:
            # 🔴 Perdemos
            dinero -= apuesta_actual
            # Doblar la apuesta para la próxima ronda (estrategia Martingala)
            apuesta_actual *= 2
    
    return {
        'exito': dinero >= objetivo,
        'dinero_final': dinero,
        'rondas': ronda,
        'ganancia': dinero - dinero_inicial
    }


# Pedir datos por teclado
print("🎲 SIMULADOR DE ESTRATEGIA MARTINGALA 🎲")
print("=" * 50)

dinero_inicial = float(input("💰 Dinero inicial: "))
apuesta_inicial = float(input("🎯 Apuesta inicial: "))
probabilidad_ganar = float(input("📊 Probabilidad de ganar (0-1): "))
objetivo = float(input("🏆 Objetivo a alcanzar: "))

usar_limite = input("¿Usar límite máximo de apuesta? (s/n): ").lower()
if usar_limite == 's':
    limite_apuesta_max = float(input("🚫 Límite máximo de apuesta: "))
else:
    limite_apuesta_max = None

print("\n" + "=" * 50)
print("🎮 INICIANDO SIMULACIÓN...")
print("=" * 50 + "\n")

# Ejecutar simulación
resultado = simular_martingala(dinero_inicial, apuesta_inicial, probabilidad_ganar, objetivo, limite_apuesta_max)

# Mostrar resultados
print("\n" + "=" * 50)
print("📊 RESULTADOS DE LA SIMULACIÓN")
print("=" * 50)

if resultado['exito']:
    print("🎉 ¡OBJETIVO ALCANZADO!")
else:
    print("💸 BANCARROTA")

print(f"\n💰 Dinero final: {resultado['dinero_final']:.2f}€")
print(f"🎲 Rondas jugadas: {resultado['rondas']}")
print(f"📈 Ganancia/Pérdida: {resultado['ganancia']:+.2f}€")
print(f"📊 Rentabilidad: {(resultado['ganancia']/dinero_inicial)*100:+.2f}%")
print("=" * 50)
