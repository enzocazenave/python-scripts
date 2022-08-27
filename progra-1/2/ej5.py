"""
    ESCRIBIR UNA FUNCION QUE RECIBA UNA LISTA COMO PARÁMETRO Y DEVUELVA TRUE SI LA LISTA ESTA ORDENADA EN FORMA ASCENDENTE
    O FALSE EN CASO CONTRARIO.
"""

def verify_list(list):
    ordered_list = sorted(list)
    reverse_list = sorted(list, reverse=True)

    return True if list == ordered_list else False if list == reverse_list else 'La lista que me pasaste no esta ordenada'

# ---------------------------------------------------------------- #

elements = int(input("Ingrese cantidad de elementos a añadir a la lista: "))

list = []

for i in range(elements):
    value = input(f'[{i}] Valor: ')

    if value.isdigit():
        list.append(int(value))
    else:
        list.append(value)

print(verify_list(list))