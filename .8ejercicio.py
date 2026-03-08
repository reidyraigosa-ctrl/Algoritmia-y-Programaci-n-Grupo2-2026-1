# Posición inicial
x = 0
y = 0

print("=== SIMULACIÓN DE MOVIMIENTO CON DADO DE 4 CARAS ===")
print(f"Posición inicial: ({x}, {y})\n")

# 10 lanzamientos manuales
for lanzamiento in range(1, 11):
    
    dado = int(input(f"Lanzamiento {lanzamiento} (ingrese un número del 1 al 4): "))
    
    if dado == 1:
        x += 1
        print("Movimiento: Derecha")
        
    elif dado == 2:
        y -= 1
        print("Movimiento: Abajo")
        
    elif dado == 3:
        x -= 1
        print("Movimiento: Izquierda")
        
    elif dado == 4:
        y += 1
        print("Movimiento: Arriba")
        
    else:
        print("Número inválido (no hay movimiento)")
    
    print(f"Posición actual: ({x}, {y})\n")

print("=== RESULTADO FINAL ===")
print(f"Posición final después de 10 lanzamientos: ({x}, {y})")