# Escribir un programa que imprima los números pares entre 0 y 200 de forma decreciente.

print("Imprimir los numeros pares entre 0 y 200 forma decreciente")

for i in reversed(range(0,201)):
    if  i%2==0:
        print(i)