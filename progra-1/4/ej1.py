"""
    Desarrollar una función que determine si una cadena de caracteres es capicúa, 
    sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
    verificar su funcionamiento.
"""

def es_capicua_1(str):
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


def es_capicua_2(str):
    capicua = True

    for i in range(len(str)):
        if str[i] != str[-i-1]:
            capicua = False
            break

    return capicua


str = input('\nIngrese una palabra para verificar si es capicua: ')

if es_capicua_1(str):
    print('\n[WHILE] La palabra (', str,') es capicua')
else:
    print('\n[WHILE] La palabra (', str,') no es capicua')

if es_capicua_2(str):
    print('\n[FOR] La palabra (', str,') es capicua')
else:
    print('\n[FOR] La palabra (', str,') no es capicua')