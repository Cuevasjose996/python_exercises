# Escribir un programa que solicite al usuario 5 números, compararlos y decir cual es mayor.

numeros=[0]


print("Este programa selecciona el valor mas alto de cinco numeros.")

numero1=input("Ingrese primer numero: ")

try:
    int(numero1)
except ValueError:
    try:
        float(numero1)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero1=float(numero1)
numeros.append(numero1)

numero2=input("Ingrese el segundo numero: ")

try:
    int(numero2)
except ValueError:
    try:
        float(numero2)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero2=float(numero2)
numeros.append(numero2)

numero3=input("Ingrese el tercer numero: ")

try:
    int(numero3)
except ValueError:
    try:
        float(numero3)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero3=float(numero3)
numeros.append(numero3)

numero4=input("Ingrese el cuarto numero: ")

try:
    int(numero4)
except ValueError:
    try:
        float(numero4)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero4=float(numero4)
numeros.append(numero4)

numero5=input("Ingrese el quinto numero: ")

try:
    int(numero5)
except ValueError:
    try:
        float(numero5)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero5=float(numero5)
numeros.append(numero5)

mayor=numeros[0]

for numero in numeros:
    if numero>mayor:
        mayor=numero

print("El mayor es el:", mayor)