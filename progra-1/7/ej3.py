"""
    Escribir una funcion que devuelva la suma de los N primeros numeros naturales.
"""

def suma_numeros(N):
    if N == 0:
        return N
    else: 
        return N + suma_numeros(N - 1)

N = int(input("Ingrese un numero: "))
print(f"La suma de los primeros { N } numeros es { suma_numeros(N) }")