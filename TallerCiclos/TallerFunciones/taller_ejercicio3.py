def agregar_producto(diccionario, nombre, cantidad, precio):
    """
    Agrega un producto al inventario o actualiza su cantidad y precio
    si el producto ya existe.
    """
    if nombre in diccionario:
        print(f"i'{nombre}' ya existe. Se actualizará su información.")
    diccionario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado/actualizado correctamente.")


def eliminar_producto(diccionario, nombre):
    "Elimina un producto del inventario por su nombre."
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no se encontró en el inventario.")


def calcular_valor_total(diccionario):
    """
    Calcula el valor total del inventario
    (suma de cantidad x precio para cada producto).
    """
    total = 0
    for producto in diccionario.values():
        total += producto["cantidad"] * producto["precio"]
    return total


def mostrar_inventario(diccionario):
    "Imprime en pantalla todos los productos del inventario."
    print("\n" + "=" * 55)
    print(f"  {'PRODUCTO':<20} {'CANTIDAD':>8}  {'PRECIO':>10}  {'SUBTOTAL':>10}")
    print("-" * 55)
    if not diccionario:
        print("  (El inventario está vacío)")
    else:
        for nombre, datos in diccionario.items():
            subtotal = datos["cantidad"] * datos["precio"]
            print(f"  {nombre:<20} {datos['cantidad']:>8}  "
                  f"${datos['precio']:>9.2f}  ${subtotal:>9.2f}")
    print("-" * 55)
    print(f"  {'VALOR TOTAL':>40}  ${calcular_valor_total(diccionario):>9.2f}")
    print("=" * 55)

#Menú interactivo
def mostrar_menu():
    print("\n" + "=" * 40)
    print("GESTIÓN DE INVENTARIO")
    print("=" * 40)
    print("  1. Agregar / actualizar producto")
    print("  2. Eliminar producto")
    print("  3. Mostrar inventario")
    print("  4. Calcular valor total")
    print("  0. Salir")
    print("=" * 40)


if __name__ == "__main__":
    # Inventario inicial de ejemplo
    inventario = {}
    agregar_producto(inventario, "Manzanas",   50,  1.20)
    agregar_producto(inventario, "Arroz 1 kg", 30,  2.50)
    agregar_producto(inventario, "Leche 1 L",  20,  1.80)
    agregar_producto(inventario, "Aceite 1 L", 15,  3.40)
    agregar_producto(inventario, "Azúcar 1 kg",25,  1.90)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            nombre   = input("Nombre del producto : ").strip()
            cantidad = int(float(input("Cantidad            : ")))
            precio   = float(input("Precio unitario ($) : "))
            agregar_producto(inventario, nombre, cantidad, precio)

        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(inventario, nombre)

        elif opcion == "3":
            mostrar_inventario(inventario)

        elif opcion == "4":
            total = calcular_valor_total(inventario)
            print(f"\nValor total del inventario: ${total:.2f}")

        else:
            print("Opción no válida. Intente de nuevo.")
