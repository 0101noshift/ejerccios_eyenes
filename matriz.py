import numpy as np
import random

"""
Crear una matriz de 5x5 randomizada con numeros enteros, encontrar secuencia de 4 numeros
consecutivos horizontal o vertical y si se encuentra mostrar la posicion inicial y final.
"""

matriz = np.random.randint(6, size=(5, 5))

print(matriz)

resultado = True
lista_ord = []

for i in matriz:
    a = True
    for ele in i:
        if len(lista_ord) != 0:
            if lista_ord[-1] != ele-1:
                a = False
                break
        lista_ord.append(ele)
        
    if not a:
        resultado = False
        break
    
print(f"Tiene consecutivos?: {str(resultado)}.")