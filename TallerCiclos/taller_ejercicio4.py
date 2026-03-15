# Alarma a las 6 AM
hora = 6
minutos = 0
boton = "no"

print("La alarma está sonando...")

while minutos < 60 and boton != "si":
    
    boton = input("¿Desea apagar la alarma? (si/no): ")
    minutos = minutos + 1

print("Alarma apagada")