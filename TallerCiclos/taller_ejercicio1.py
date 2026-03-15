n = int(input("Ingrese un número: "))

print("Cuadrados menores que n:")
i = 0
while i * i < n:
    print(i * i)
    i = i + 1


print("Divisibles por 10 menores que n:")
i = 10
while i < n:
    print(i)
    i = i + 10


print("Potencias de 2 menores que n:")
i = 1
while i < n:
    print(i)
    i = i * 2