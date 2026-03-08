# Precio por kWh
precio_kwh = 0.15

# Lista para guardar los clientes
clientes = []

# Cantidad de clientes
cantidad = int(input("¿Cuántos clientes desea registrar? "))

for i in range(cantidad):
    print("\nCliente", i + 1)
    
    nombre = input("Ingrese el nombre del cliente: ")
    consumo = float(input("Ingrese el consumo en kWh: "))
    
    # Calcular costo
    costo = consumo * precio_kwh
    
    # Diccionario del cliente
    cliente = {
        "nombre": nombre,
        "consumo": consumo,
        "costo": costo
    }
    
    # Guardar en la lista
    clientes.append(cliente)

# Mostrar resultados
print("\n=== REGISTRO DE CLIENTES ===")

for cliente in clientes:
    print("Nombre:", cliente["nombre"])
    print("Consumo:", cliente["consumo"], "kWh")
    
    # Condicional solo como ejemplo de uso
    if cliente["consumo"] > 500:
        print("Consumo alto")
    else:
        print("Consumo normal")
    
    print("Total a pagar: $", cliente["costo"])
    print("----------------------")