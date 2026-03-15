x = 0
y = 0
pasos = 0

print("Posición inicial:", x, y)
print("Direcciones: 1=arriba, 2=abajo, 3=derecha, 4=izquierda")

while pasos < 100:

    direccion = int(input("Ingrese una dirección (1-4): "))

    if direccion == 1:
        y = y + 1
    elif direccion == 2:
        y = y - 1
    elif direccion == 3:
        x = x + 1
    elif direccion == 4:
        x = x - 1

    pasos = pasos + 1

print("Ubicación final:", x, y)