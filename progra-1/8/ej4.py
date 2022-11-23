"""
    4. Escribir una función que indique si dos fichas de dominó encajan o no. 
    Las fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). 
    La función devuelve True o False. Escribir también un programa para 
    verificar su comportamiento.
"""

from random import randint

def verificar_fichas(ficha_1, ficha_2):
    return (
        ficha_1[1] == ficha_2[0] or
        ficha_1[0] == ficha_2[1] or
        ficha_1[1] == ficha_2[1] or
        ficha_1[0] == ficha_2[0]
    )

# Programa para verificar comportamiento
ficha_random_1 = (randint(1,6), randint(1,6))
ficha_random_2 = (randint(1,6), randint(1,6))

if verificar_fichas(ficha_random_1, ficha_random_2):
    print(f"Las fichas { ficha_random_1 } y { ficha_random_2 } encajan")
else:
    print(f"Las fichas { ficha_random_1 } y { ficha_random_2 } no encajan")