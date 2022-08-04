import random
from operator import itemgetter

"""
Hacer una funcion que genere una lista de diccionarios que contengan id y edad, donde edad sea un numero
aleatorio entre 1 y 100 y la longitud de la lista sea de 10 elementos. retornar la lista.

Hacer otra funcion que reciba lo generado en la primera funcion y ordernarlo de mayor a menor.
Printear el id de la persona mas joven y mas vieja. Devolver la lista ordenada.
"""

def generar_lista():
    lista = []
    for x in range(1,11):
        persona = {
        'id': x,
        'edad': random.randint(1,101)    
        }
        lista.append(persona)
    return lista

print(f"Este es la primer lista: \n{generar_lista()}.")

print("===================================================================")

def ordenar_lista(lista):
    lista.sort(reverse=True, key=itemgetter('edad'))
    vieja = lista[1]
    joven = lista[-1]
    print(f"Esta lista se encuentra ordenada: \n{lista}.")
    print(f"La persona mas vieja es: \n{lista[1]} \ny la persna mas joven es: \n{lista[-1]}.")

print(f"Esta es la segunda lista: \n{ordenar_lista(generar_lista())}.")