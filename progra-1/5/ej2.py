"""
    Ejercicio 2

    Realizar una funcion que reciba como parámetros dos CADENAS DE CARACTERES conteniendo
    numeros reales, sume ambos valores y devuelva el resultado como un numero real. 
    Devolver -1 si alguna de las cadenas no contiene un numero valido, utilizando manejo de
    excepciones para detectar el error.
"""

def suma_valores(a, b):
    try:
        a_int = int(a)
        b_int = int(b)

        return a_int + b_int
    except ValueError:
        return "-1"
    

a = input("Ingrese un numero A: ")
b = input("Ingrese un numero B: ")
c = suma_valores(a, b)

print(c)

