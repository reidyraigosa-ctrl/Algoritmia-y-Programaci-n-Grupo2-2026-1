print("A → Amarillo")
print("M → Morado")
print("N → Naranja")

opcion = input("Ingrese su voto: ").upper()

if opcion == "A":
    print("Usted ha votado por el partido Amarillo")

elif opcion == "M":
    print("Usted ha votado por el partido Morado")

elif opcion == "N":
    print("Usted ha votado por el partido Naranja")

else:
    print("Opción errónea")