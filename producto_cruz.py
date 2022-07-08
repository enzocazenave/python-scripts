print()
print("Bienvenido a la calculadora de producto vectorial automatico. Los vectores se deben ingresar de la siguiente manera: 2 1 9")
print()

vector1 = list(map(int, input("Ingrese vector A: ").split(" ")))
vector2 = list(map(int, input("Ingrese vector B: ").split(" ")))

resultado = []

for i in range(len(vector1)):
    toAppend = 0

    if i == 0:
        toAppend = (vector1[1] * vector2[2]) - (vector2[1] * vector1[2])
    elif i == 1:
        toAppend = -((vector1[0] * vector2[2]) - (vector2[0] * vector1[2]))
    elif i == 2:
        toAppend = (vector1[0] * vector2[1]) - (vector2[0] * vector1[1])

    resultado.append(toAppend)

print()

print("VECTORES INGRESADOS")
print(f"A: {vector1}")
print(f"B: {vector2}")

print()

print(f"El resultado de AxB es {resultado}")