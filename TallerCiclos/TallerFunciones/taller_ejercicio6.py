PRODUCTOS = {
    "Agua 500 mL":    1500,
    "Gaseosa 350 mL": 2500,
    "Jugo de naranja":3000,
    "Café caliente":  2000,
    "Snack de maíz":  1800,
}

def mostrar_productos():
    "Muestra el menú de productos disponibles con sus precios."
    print("\n" + "=" * 40)
    print("MÁQUINA DISPENSADORA")
    print("=" * 40)
    for i, (nombre, precio) in enumerate(PRODUCTOS.items(), 1):
        print(f"  {i}. {nombre:<20}  $ {precio:,}")
    print("  0. Salir")
    print("=" * 40)

def seleccionar_producto():
    """
    Permite al usuario escoger un producto.
    Retorna (nombre, precio) del producto seleccionado, o (None, None) para salir.
    """
    nombres = list(PRODUCTOS.keys())
    while True:
        opcion = input("Selecciona el número de producto: ").strip()
        if opcion == "0":
            return None, None
        if opcion.isdigit() and 1 <= int(opcion) <= len(nombres):
            nombre = nombres[int(opcion) - 1]
            return nombre, PRODUCTOS[nombre]
        print(f"Opción inválida. Elige entre 1 y {len(nombres)}, o 0 para salir.")

def leer_pago(precio_producto):
    """
    Solicita el dinero ingresado por el usuario.
    Retorna el valor ingresado como entero.
    """
    while True:
        try:
            pago = int(input(f"Ingresa el dinero (precio: $ {precio_producto:,}): $ "))
            return pago
        except ValueError:
            print("Por favor ingresa un valor numérico entero.")

def verificar_pago_insuficiente(pago, precio):
    """
    Bonus: Verifica si el pago es menor al precio del producto.
    Retorna True si el pago es insuficiente, False si es suficiente.
    """
    if pago < precio:
        faltante = precio - pago
        print(f"\n Pago insuficiente. Te faltan $ {faltante:,} para completar la compra.")
        return True
    return False

def calcular_devuelta(pago, precio):
    "Calcula el valor a devolver al usuario."
    return pago - precio

def dispensar(nombre_producto, pago, precio):
    """
    Realiza el cobro, verifica el pago y entrega el producto o devuelve el dinero.
    """
    # Bonus: verificar pago insuficiente
    if verificar_pago_insuficiente(pago, precio):
        return
    devuelta = calcular_devuelta(pago, precio)
    print("\n" + "" * 20)
    print(f"Producto despachado: {nombre_producto}")
    print(f"Precio: $ {precio:,}")
    print(f"Pago recibido: $ {pago:,}")

    if devuelta > 0:
        print(f" Cambio a devolver: $ {devuelta:,}")
    else:
        print("Pago exacto. ¡Sin cambio!")

    print("" * 20)
    print("Disfruta tu producto")

#Programa principal
if __name__ == "__main__":
    while True:
        mostrar_productos()
        nombre, precio = seleccionar_producto()

        if nombre is None:
            print("¡Hasta pronto! Gracias por usar la máquina.")
            break

        pago = leer_pago(precio)
        dispensar(nombre, pago, precio)

        continuar = input("\n¿Deseas comprar otro producto? (s/n): ").strip().lower()
        if continuar != "s":
            print("Hasta pronto")
            break
