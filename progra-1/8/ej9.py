"""
    9. Escribir una función que reciba un número entero N y devuelva un 
    diccionario con la tabla de multiplicar de N del 1 al 12. Escribir también 
    un programa para probar la función.
"""

def calcular_tabla(n):
    return { f"{n}x{i}":n*i for i in range(1, 13) }

# Programa para verificar el comportamiento
n = int(input("Ingrese un numero entero: "))
print(calcular_tabla(n))