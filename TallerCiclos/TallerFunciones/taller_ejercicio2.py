
#Operaciones básicas 
def suma(a, b):
    "Retorna la suma de a y b."
    return a + b

def resta(a, b):
    "Retorna la resta de a menos b."
    return a - b

def multiplicacion(a, b):
    """Retorna el producto de a y b."""
    return a * b

def division(a, b):
    "Retorna el cociente de a entre b. Evita división por cero."
    if b == 0:
        print(" Error: no se puede dividir entre cero.")
        return None
    return a / b

def operacion(a, b, op):
    "Ejecuta la operación indicada por el símbolo op (+, -, *, /)."
    operaciones = {
        "+": suma,
        "-": resta,
        "*": multiplicacion,
        "/": division
    }
    if op not in operaciones:
        print(f"Operación '{op}' no reconocida.")
        return None
    return operaciones[op](a, b)

# Potencia y raíz
def exponente(base, exp):
    """
    Calcula la base^exp usando únicamente la función multiplicacion().
    Solo soporta exponentes enteros no negativos.
    """
    if not isinstance(exp, int) or exp < 0:
        print("El exponente debe ser un entero no negativo.")
        return None
    resultado = 1
    for _ in range(exp):
        resultado = multiplicacion(resultado, base)
    return resultado

def raiz_cuadrada(numero):
    """
    Calcula √número usando exponente() con el método de Newton-Raphson.
    Depende de multiplicacion() a través de exponente().
    """
    if numero < 0:
        print("No existe raíz cuadrada real de un número negativo.")
        return None
    if numero == 0:
        return 0
    
    aproximacion = numero / 2.0
    for _ in range(100):
        aproximacion = (aproximacion + numero / aproximacion) / 2.0
    return aproximacion

# Factorial
def factorial(n):
    "Calcula n! de forma iterativa. Solo para enteros no negativos."
    if not isinstance(n, int) or n < 0:
        print("El factorial solo está definido para enteros no negativos.")
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado = multiplicacion(resultado, i)
    return resultado

#Inversa 
def inversa(numero):
    """Calcula 1/numero (la inversa multiplicativa)."""
    return division(1, numero)

# Menú interactivo 

def mostrar_menu():
    print("\n" + "=" * 45)
    print("ALCULADORA NIVEL 2")
    print("=" * 45)
    print("  1. Suma             2. Resta")
    print("  3. Multiplicación   4. División")
    print("  5. Raíz cuadrada    6. Exponente")
    print("  7. Factorial        8. Inversa")
    print("  0. Salir")
    print("=" * 45)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion in ("1", "2", "3", "4"):
            a = float(input("Ingrese el primer número : "))
            b = float(input("Ingrese el segundo número: "))
            ops = {"1": "+", "2": "-", "3": "*", "4": "/"}
            resultado = operacion(a, b, ops[opcion])
            if resultado is not None:
                print(f"Resultado: {resultado}")

        elif opcion == "5":
            a = float(input("Ingrese el número: "))
            resultado = raiz_cuadrada(a)
            if resultado is not None:
                print(f"√{a} = {resultado:.6f}")

        elif opcion == "6":
            base = float(input("Ingrese la base    : "))
            exp  = int(input("Ingrese el exponente (entero ≥ 0): "))
            resultado = exponente(base, exp)
            if resultado is not None:
                print(f"{base}^{exp} = {resultado}")

        elif opcion == "7":
            n = int(input("Ingrese el número entero: "))
            resultado = factorial(n)
            if resultado is not None:
                print(f"{n}! = {resultado}")

        elif opcion == "8":
            a = float(input("Ingrese el número: "))
            resultado = inversa(a)
            if resultado is not None:
                print(f"Inversa de {a} = {resultado}")

        else:
            print("Opción no válida. Intente de nuevo.")