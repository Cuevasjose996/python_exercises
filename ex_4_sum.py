# Escribir un programa que lea un entero positivo, 
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1. 
# La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:

valor=input("Ingrese un valor entero: ")

try: 
    int(valor)
    si= True
except ValueError:
    si= False

if si== False:
    print("Error!, ingresa un numero entero.")
elif si==True:
    valor=int(valor)
    suma=((valor*(valor+1))/2)
    print(suma)