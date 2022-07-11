# Escribir un programa que solicite al usuario un número entero y 
# muestre en pantalla si el número es Positivo (+) o Negativo (-). 
# En caso de que el número sea igual a cero (0) se debe mostrar en pantalla: 
# El número no es Positivo ni Negativo.

numero= input("Ingrese un numero entero: ")

try:
    int(numero)
    si=True
except ValueError:
    si=False

if si==True:
    numero=int(numero)
    if numero==0:
        print("El numero no es positivo ni negativo.")
    elif numero>0:
        print("El numero es positivo")
    elif 0>numero:
        print("El numero es negativo")
else:
    print("Error! Ingrese un numero entero.")