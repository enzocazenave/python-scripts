def calcular_vuelto(precio, dinero_recibido):
    billetes = [500, 100, 50, 20, 10, 5, 1]
    
    if dinero_recibido >= precio:
        vuelto = dinero_recibido - precio

        for billete in billetes:
            print(f"{vuelto // billete} billetes de {billete}")
            vuelto %= billete

    else:
        print("[PROGRAMA] El dinero es insuficiente")

calcular_vuelto(200,520)