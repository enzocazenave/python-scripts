"""
    Resolver el siguiente problema, utilizando funciones:

    Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco dígitos
    hasta ingresar un cero como fin de carga. Se solicita:
    
    a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
    b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de entrada al club antes y después de
    eliminarlo. Informar cuántos ingresos se eliminaron.
"""

socios = []
informe = []

def registrar_socio(numero):
    if numero >= 10000 and numero <= 99999:
        socios.append(numero)
    else:
        print("El numero de socio ingresado no es correcto")


def dar_de_baja():
    numero = int(input('\nIngrese numero de socio a dar de baja: '))
    print(f"\nEstas seguro que quieres dar de baja al socio {numero}?\nS = Si\nN = No")
    opcion = input()

    if opcion == "S":
        if numero >= 10000 and numero <= 99999:
            encontrado = False

            for i in range(len(informe)):
                if numero == informe[i][0]:
                    print(f"\nEl socio {informe[i][0]} que diste de baja ingreso al club {informe[i][1]} veces")
                    informe.remove(informe[i])
                    encontrado = True
                    break

            if not encontrado:
                print("\nNo existe ese numero de socio, fin del programa.")
        else:
            print("Numero de socio incorrecto, fin del programa.")
    elif opcion == "N":
        print("Fin del programa")
    else:
        print("Opcion no valida, fin del programa.")


def mostrar_informe():
    for numero_socio in socios:
        socio = [numero_socio, socios.count(numero_socio)]

        if not socio in informe:
            informe.append(socio)

    print("\nINGRESOS AL CLUB\n")

    for fila in informe:
        for columna in fila:
            print("%3d" %columna, end='') 
        print()


flag = True

while flag:
    numero_de_socio = int(input('Ingrese numero de socio: '))
    
    if numero_de_socio != 0:
        registrar_socio(numero_de_socio)
    else: 
        mostrar_informe()
        dar_de_baja()
        flag = False