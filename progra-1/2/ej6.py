"""
    ESCRIBIR UNA FUNCION QUE RECIBA UNA LISTA COMO PARÁMETRO Y LA NORMALICE, ES DECIR QUE TODOS SUS ELEMENTOS DEBEN SUMAR 1
"""

def normalize_list(list):
    normalized_list = list.copy()
    suma = sum(normalized_list)

    for i in range(len(normalized_list)):
        normalized_list[i] /= suma

    return normalized_list

# ---------------------------------------------------------------- #

elements = int(input("Ingrese cantidad de elementos a añadir a la lista: "))

list = []

for i in range(elements):
    value = int(input(f'[{i}] Valor: '))
    list.append(value)

print(normalize_list(list))