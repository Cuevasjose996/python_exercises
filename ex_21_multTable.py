# Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de multiplicar del 1 al 10 del valor introducido.

valor=input("Ingrese un numero entero: ")

try:
    int(valor)
except ValueError:
    print("Error! Ingrese un numero entero.")
    exit()

valor=int(valor)

for i in range(1,11):
    multiplicacion=valor*(i)
    print ("{}x{}={}".format(valor,i,multiplicacion))