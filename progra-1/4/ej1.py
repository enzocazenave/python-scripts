def es_capicua(str):
    cont = 0
    cont_invertido = len(str) - 1

    while str[cont] == str[cont_invertido]:
        if cont == cont_invertido:
            return True
        
        cont += 1
        cont_invertido -= 1

    return False


str = input('\nIngrese una palabra para verificar si es capicua: ')

if es_capicua(str):
    print('\nLa palabra (', str,') es capicua')
else:
    print('\nLa palabra (', str,') no es capicua')