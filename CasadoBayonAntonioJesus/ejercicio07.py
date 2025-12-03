# Implementa una función modo_avion(texto, activar=True) que reciba una cadena y un booleano.
# - Si activar es True, devuelve la cadena "[MODO AVIÓN] " seguida del texto.
# - Si activar es False, devuelve solo el texto original.

def modo_avion(texto, activar=True):
    
    if activar == True:
        return "[MODO AVIÓN] " + texto
    else:
        
        return texto



print(modo_avion("Mensaje importante"))
print(modo_avion("Mensaje importante", True))
print(modo_avion("Mensaje importante", False))
print(modo_avion("Bienvenido"))
print(modo_avion("Bienvenido", activar=False))
