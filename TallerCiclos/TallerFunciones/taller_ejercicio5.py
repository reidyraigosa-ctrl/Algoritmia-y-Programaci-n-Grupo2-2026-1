
import random

DIFICULTADES = {
    "1": {"nombre": "Fácil",  "intentos": 10},
    "2": {"nombre": "Medio",  "intentos": 6},
    "3": {"nombre": "Difícil","intentos": 3},
}

historial = []   # Bonus: guarda resultados de cada partida


def elegir_dificultad():
    """
    Solicita al usuario que elija un nivel de dificultad.
    Retorna el número de intentos disponibles y el nombre del nivel.
    """
    print("\n Elige el nivel de dificultad:")
    for clave, datos in DIFICULTADES.items():
        print(f"  {clave}. {datos['nombre']}  ({datos['intentos']} intentos)")

    while True:
        opcion = input("Selecciona (1/2/3): ").strip()
        if opcion in DIFICULTADES:
            nivel = DIFICULTADES[opcion]
            print(f"Nivel seleccionado: {nivel['nombre']}")
            return nivel["intentos"], nivel["nombre"]
        print("Opción inválida. Intenta de nuevo.")


def generar_numero(minimo=1, maximo=100):
    "Genera y retorna un número entero aleatorio en [minimo, maximo]."
    return random.randint(minimo, maximo)


def jugar(intentos_totales):
    """
    Lógica principal del juego.
    Retorna True si el jugador ganó, False si perdió, junto con el número secreto.
    """
    secreto = generar_numero()
    intentos_restantes = intentos_totales

    print(f"\n He elegido un número entre 1 y 100. ¡Tienes {intentos_totales} intentos!")

    while intentos_restantes > 0:
        print(f"\n Intentos restantes: {intentos_restantes}")
        try:
            intento = int(input("¿Cuál es tu número? "))
        except ValueError:
            print("Por favor ingresa un número entero.")
            continue

        if intento == secreto:
            usados = intentos_totales - intentos_restantes + 1
            print(f"\n Correcto. El número era {secreto}. Lo lograste en {usados} intento(s).")
            return True, secreto, usados

        elif intento < secreto:
            print(" El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")

        intentos_restantes -= 1

    print(f"\n ¡Se acabaron los intentos! El número secreto era {secreto}.")
    return False, secreto, intentos_totales


def guardar_historial(nombre_nivel, gano, secreto, intentos_usados):
    "Bonus: agrega el resultado al historial en memoria y en un archivo .txt."
    resultado = {
        "nivel":   nombre_nivel,
        "gano":    gano,
        "numero":  secreto,
        "intentos": intentos_usados,
    }
    historial.append(resultado)

    # Guardar en archivo
    with open("historial_juego.txt", "a", encoding="utf-8") as f:
        estado = "GANÓ" if gano else "PERDIÓ"
        f.write(f"Nivel: {nombre_nivel} | Número: {secreto} | "
                f"Intentos usados: {intentos_usados} | {estado}\n")


def mostrar_historial():
    "Bonus: muestra el historial de partidas."
    if not historial:
        print("\n No hay partidas registradas aún.")
        return
    print("\n Historial de partidas:")
    print("-" * 45)
    for i, r in enumerate(historial, 1):
        estado = "GANÓ" if r["gano"] else "PERDIÓ"
        print(f"  {i}. [{r['nivel']}] Número {r['numero']} | "
              f"{r['intentos']} intento(s) | {estado}")
    print("-" * 45)


# ── Programa principal ──────────────────────────────────────
if __name__ == "__main__":
    print("=" * 45)
    print(" JUEGO: ADIVINA EL NÚMERO")
    print("=" * 45)

    while True:
        intentos, nivel_nombre = elegir_dificultad()
        gano, numero, usados   = jugar(intentos)
        guardar_historial(nivel_nombre, gano, numero, usados)

        print("\n¿Qué deseas hacer?")
        print("  1. Jugar de nuevo")
        print("  2. Ver historial")
        print("  0. Salir")
        opcion = input("Selecciona: ").strip()

        if opcion == "2":
            mostrar_historial()
        elif opcion == "0":
            print("Gracias por jugar")
            break
