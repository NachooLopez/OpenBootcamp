import time

tiempo_actual = time.localtime()
hora_actual = int(time.strftime("%H", tiempo_actual))

if hora_actual >= 19:
    print("¡Se ha acabado la jornada, es hora de volver a casa!")
else:
    print(f"¡Aún faltan {19 - hora_actual} horas para volver a casa!")
