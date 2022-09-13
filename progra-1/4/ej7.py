"""
    Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir
    de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. 
    Escribir tambien un programa para verificar el comportamiento de la misma.

    Escribir una funcion para cada uno de los siguientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanada
"""

def probar_funcion(metodo):
    string = input('\nIngrese cadena de texto: ')
    pos_1 = int(input('Numero posicion 1: '))
    pos_2 = int(input('Numero de posicion 2: '))

    if metodo == 1:
        return a_eliminar_subcadena(string, pos_1, pos_2)
    else:
        return b_eliminar_subcadena(string, pos_1, pos_2)

def a_eliminar_subcadena(str, pos_1, pos_2):
    return str[:pos_1] + str[pos_2:]

def b_eliminar_subcadena(str, pos_1, pos_2):
    new_str = ""

    for i in range(len(str)):
        if i < pos_1 or i >= pos_2:
            new_str += str[i]

    return new_str

metodo = int(input('''
¿Qué método para eliminar una subcadena quieres utilizar?
1. Utilizando rebanadas
2. Sin utlizar rebanadas  
'''))

if metodo == 1 or metodo == 2:
    resultado = probar_funcion(metodo)
    print('\n----- RESULTADO -----')
    print(resultado)
else:
    print("Ese método no existe.")