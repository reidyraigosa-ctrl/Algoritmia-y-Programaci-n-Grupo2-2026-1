#1. Potencias de 2 desde 2⁰ hasta 2²⁰
i = 0

while i <= 20:
    print(2**i)
    i = i + 1

#2. Suma de números impares entre a y b
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

suma = 0
i = a

while i <= b:
    if i % 2 != 0:
        suma = suma + i
    i = i + 1

print("Resultado:", suma)

#3. Suma de los dígitos impares de un número
n = int(input("Ingrese un número: "))

suma = 0

while n > 0:
    digito = n % 10
    
    if digito % 2 != 0:
        suma = suma + digito
    
    n = n // 10

print("Resultado:", suma)
