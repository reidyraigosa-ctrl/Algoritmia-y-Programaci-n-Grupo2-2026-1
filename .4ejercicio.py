nivel = 10
valvula = False

print("Nivel inicial:", nivel)

# Persona extrae agua
nivel -= 10

if nivel <= 0:
    nivel = 0
    valvula = True
    print("Tanque vacío → Válvula ABIERTA")

# Entra agua si la válvula está abierta
if valvula == True:
    nivel += 100

if nivel >= 100:
    nivel = 100
    valvula = False
    print("Tanque lleno → Válvula CERRADA")

print("Nivel final:", nivel)