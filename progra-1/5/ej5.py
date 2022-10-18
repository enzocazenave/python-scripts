"""
    Ejercicio 5

    La raiz cuadrada de un numero puede obtenerse mediante la funcion sqrt() del modulo math.
    Escribir un programa que utilice esta funcion para calcular la raiz de un numero cualquiera
    ingresado a traves de teclado. El programa debe utilizar manejo de excepciones para evitar
    errores si se ingresa un numero negativo.
"""

from math import sqrt

while True:
    try:
        n = int(input("Ingrese un numero: "))

        assert n >= 0, "[ERROR] No se pueden ingresar numeros negativos."

        print(f"La raiz cuadrada de {n} es {sqrt(n)}")
        break
    except AssertionError as message:
        print(message)