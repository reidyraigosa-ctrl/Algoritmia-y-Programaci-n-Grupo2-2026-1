# Inventario de la tienda
inventario = {
    "Manzana": 2.5,
    "Banana": 1.8,
    "Naranja": 3.0,
    "Pera": 2.0,
    "Monster": 5.0,
    "Agua": 1.0,
    "Coca-Cola": 3.5
}

print("1. Verificar producto")
print("2. Agregar producto")
print("3. Eliminar producto")
print("4. Actualizar precio")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    producto = input("Ingrese el nombre del producto: ")
    if producto in inventario:
        print("El producto está en el inventario y cuesta $", inventario[producto])
    else:
        print("El producto no está en el inventario")

elif opcion == 2:
    producto = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    inventario[producto] = precio
    print("Producto agregado")

elif opcion == 3:
    producto = input("Producto a eliminar: ")
    if producto in inventario:
        del inventario[producto]
        print("Producto eliminado")
    else:
        print("El producto no existe")

elif opcion == 4:
    producto = input("Producto a actualizar: ")
    if producto in inventario:
        precio = float(input("Nuevo precio: "))
        inventario[producto] = precio
        print("Precio actualizado")
    else:
        print("El producto no existe")

print("Inventario actual:", inventario)