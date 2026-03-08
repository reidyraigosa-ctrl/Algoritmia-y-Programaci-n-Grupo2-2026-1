num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
op = input("Ingrese la operación (+, -, *, /): ")

if op == "+":
    print("Resultado:", num1 + num2)

elif op == "-":
    print("Resultado:", num1 - num2)

elif op == "*":
    print("Resultado:", num1 * num2)

elif op == "/":
    if num2 == 0:
        print("Error: No se puede dividir entre cero")
    else:
        print("Resultado:", num1 / num2)

else:
    print("Operación no válida")