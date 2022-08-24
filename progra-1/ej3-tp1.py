def revisar_tarifa(viajes):
    precio_viaje = 30

    if viajes >= 21 and viajes <= 30:
        precio_viaje *= 0.80
    elif viajes >= 31 and viajes <= 40:
        precio_viaje *= 0.70
    elif viajes >= 41:
        precio_viaje *= 0.60

    return viajes * precio_viaje

print(f"El gasto total de viajes es ${revisar_tarifa(32)}")


