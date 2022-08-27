def normalize_list(list):
    normalized_array = list.copy()
    suma = sum(normalized_array)

    for i in range(len(normalized_array)):
        normalized_array[i] /= suma

    return normalized_array

# ---------------------------------------------------------------- #

elements = int(input("Ingrese cantidad de elementos a añadir a la lista: "))

list = []

for i in range(elements):
    value = int(input(f'[{i}] Valor: '))
    list.append(value)

print(normalize_list(list))