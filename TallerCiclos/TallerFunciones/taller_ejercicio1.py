
def promedio(lista):
    "Calcula la temperatura promedio de la lista."
    return sum(lista) / len(lista)

def extremos(lista):
    "Retorna la temperatura más alta y más baja."
    return max(lista), min(lista)

def dias_sobre_promedio(lista):
    "Cuenta cuántas horas la temperatura estuvo por encima del promedio."
    prom = promedio(lista)
    contador = 0
    for temp in lista:
        if temp > prom:
            contador += 1
    return contador

def mostrar_resultados(lista):
    "Muestra todos los análisis de la lista de temperaturas."
    print("=" * 50)
    print("   ANÁLISIS DE TEMPERATURAS DEL DÍA (°C)")
    print("=" * 50)

    print("\nTemperaturas por hora:")
    for hora, temp in enumerate(lista):
        print(f"  {hora:02d}:00 h  →  {temp} °C")

    prom = promedio(lista)
    temp_max, temp_min = extremos(lista)
    horas_sobre = dias_sobre_promedio(lista)

    print(f"\n Temperatura promedio   : {prom:.2f} °C")
    print(f" Temperatura más alta   : {temp_max} °C  (hora {lista.index(temp_max):02d}:00)")
    print(f"Temperatura más baja   : {temp_min} °C  (hora {lista.index(temp_min):02d}:00)")
    print(f"⬆Horas sobre el promedio: {horas_sobre} de {len(lista)}")
    print("=" * 50)

#Programa principal
if __name__ == "__main__":
    # Lista de 24 temperaturas (una por hora, 00:00 – 23:00)
    temperaturas = [
        15.2, 14.8, 14.3, 14.0, 13.7, 13.5,   # 00 – 05
        14.1, 15.6, 17.3, 19.8, 21.4, 23.0,   # 06 – 11
        24.5, 25.1, 25.8, 25.3, 24.7, 23.9,   # 12 – 17
        22.4, 20.6, 19.1, 18.0, 17.2, 16.4    # 18 – 23
    ]

    mostrar_resultados(temperaturas)