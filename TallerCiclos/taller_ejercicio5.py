valvula = "cerrada"

while True:

    vacio = input("¿El tanque está vacío? (si/no): ")

    if vacio == "si":
        valvula = "abierta"
        print("La válvula se abre y el tanque empieza a llenarse")

    lleno = input("¿El tanque está lleno? (si/no): ")

    if lleno == "si":
        valvula = "cerrada"
        print("El tanque está lleno, la válvula se cierra")
        break