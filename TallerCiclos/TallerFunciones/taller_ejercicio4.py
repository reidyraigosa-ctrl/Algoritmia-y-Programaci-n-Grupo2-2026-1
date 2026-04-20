PESOS = [0.30, 0.30, 0.40]
NOTA_APROBACION = 3.0

notas = {
    "Harry":    [3.8, 4.0, 4.2],
    "Ron":      [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Draco":    [4.5, 4.2, 5.0],
    "Neville":  [2.5, 3.0, 3.2],
}


def promedio_simple(lista_notas):
    "Calcula el promedio aritmético simple de las notas."
    return sum(lista_notas) / len(lista_notas)


def promedio_ponderado(lista_notas, pesos=PESOS):
    "Calcula el promedio ponderado usando los pesos dados."
    return sum(n * p for n, p in zip(lista_notas, pesos))


def mejor_estudiante(diccionario_notas):
    "Retorna el nombre del estudiante con el mayor promedio ponderado."
    mejor = max(diccionario_notas, key=lambda est: promedio_ponderado(diccionario_notas[est]))
    return mejor, promedio_ponderado(diccionario_notas[mejor])


def estudiantes_aprobados(diccionario_notas):
    "Retorna una lista con los nombres de los estudiantes aprobados (≥ 3.0)."
    aprobados = []
    for estudiante, notas_est in diccionario_notas.items():
        if promedio_ponderado(notas_est) >= NOTA_APROBACION:
            aprobados.append(estudiante)
    return aprobados


def mostrar_reporte(diccionario_notas):
    "Imprime el reporte completo de notas."
    print("\n" + "=" * 65)
    print("REPORTE DE NOTAS – CLASE PROF. McGONAGALL")
    print("=" * 65)
    print(f"  {'ESTUDIANTE':<12} {'N1':>5} {'N2':>5} {'N3':>5}  "
          f"{'P.SIMPLE':>9}  {'P.PONDER':>9}  {'ESTADO':>10}")
    print("-" * 65)

    for estudiante, notas_est in diccionario_notas.items():
        p_simple   = promedio_simple(notas_est)
        p_ponder   = promedio_ponderado(notas_est)
        aprobado   = p_ponder >= NOTA_APROBACION
        estado_txt = "APROBÓ" if aprobado else "REPROBÓ"
        print(f"  {estudiante:<12} "
              f"{notas_est[0]:>5.1f} {notas_est[1]:>5.1f} {notas_est[2]:>5.1f}  "
              f"{p_simple:>9.2f}  {p_ponder:>9.2f}  {estado_txt:>10}")

    print("=" * 65)

    # Mejor estudiante
    nombre_mejor, prom_mejor = mejor_estudiante(diccionario_notas)
    print(f"\n Mejor promedio ponderado: {nombre_mejor} ({prom_mejor:.2f})")

    # Mensaje Mcgonagall (bonus)
    print("\nMensaje de la Profesora McGonagall:")
    print("-" * 65)
    for estudiante, notas_est in diccionario_notas.items():
        p_ponder = promedio_ponderado(notas_est)
        if p_ponder >= NOTA_APROBACION:
            print(f"{estudiante}: CURSO APROBADO {p_ponder:.2f}.")
        else:
            print(f"{estudiante}: CURSO REPROBADO ({p_ponder:.2f} < 3.0).")
    print("=" * 65)

#Programa principal
if __name__ == "__main__":
    mostrar_reporte(notas)
