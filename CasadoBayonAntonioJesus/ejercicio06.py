#Escribe una función filtrar_calorias (lista_comidas, max_calorias) que reciba una lista de tuplas
#(nombre_comida, calorías) y devuelva una nueva lista solo con las comidas cuya cantidad de calorías
#sea menor o igual que max_calorias. Si la lista está vacía, devuelve una lista vacía.


comidas = [
    ("Ensalada", 150),
    ("Pizza", 800),
    ("Manzana", 95),
    ("Hamburguesa", 650),
    ("Yogur", 120)
]

def filtrar_calorias(lista_comidas, max_calorias):
   
    if lista_comidas == []:
        return []
    
    
    comidas_filtradas = []
    
    
    for comida in lista_comidas:
        nombre = comida[0]  
        calorias = comida[1]  
        
        
        if calorias <= max_calorias:
            comidas_filtradas.append(comida)
    
    
    return comidas_filtradas





print("Lista original:", comidas)
print("\nComidas con máximo 200 calorías:")
print(filtrar_calorias(comidas, 200))

print("\nComidas con máximo 500 calorías:")
print(filtrar_calorias(comidas, 500))

print("\nLista vacía:")
print(filtrar_calorias([], 300))
