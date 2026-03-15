#Suma de todos los números pares entre 2 y 100
suma = 0
i = 2

while i <= 100:
    suma = suma + i
    i = i + 2

print("La suma de los números pares es:", suma)

#Suma de todos los cuadrados entre 1 y 100
suma = 0
i = 1

while i <= 100:
    suma = suma + i*i
    i = i + 1

print("La suma de los cuadrados es:", suma)

#Suma de números impares entre a y b
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

suma = 0
i = a

while i <= b:
    if i % 2 != 0:
        suma = suma + i
    i = i + 1

print("La suma de los impares es:", suma)

#Suma de los dígitos impares de un número
n = int(input("Ingrese un número: "))

suma = 0

while n > 0:
    digito = n % 10
    
    if digito % 2 != 0:
        suma = suma + digito
    
    n = n // 10

print("La suma de los dígitos impares es:", suma)
