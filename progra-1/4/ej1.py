"""
    Desarrollar una función que determine si una cadena de caracteres es capicúa, 
    sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
    verificar su funcionamiento.
"""

def es_capicua(str):
    cont = 0
    cont_invertido = len(str) - 1
    capicua = False

    while str[cont] == str[cont_invertido]:
        if cont == cont_invertido:
            capicua = True
            break
        
        cont += 1
        cont_invertido -= 1

    return capicua


str = input('\nIngrese una palabra para verificar si es capicua: ')

if es_capicua(str):
    print('\nLa palabra (', str,') es capicua')
else:
    print('\nLa palabra (', str,') no es capicua')