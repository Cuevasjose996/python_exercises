# Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.

valor=input("Ingresa un numero entero y positivo: ")

try:
    int(valor)
except ValueError:
    print("Error! Ingresa un numero entero.")
    exit()

valor=int(valor)

print("Imprimir los numeros pares hasta tu valor")

if valor<=0:
    print("Ingresa un valor positivo.")
elif 0<valor:
    for i in range(1,valor+1):
        if  i%2==0:
            print(i)