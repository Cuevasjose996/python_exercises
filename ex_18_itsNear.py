# Escribir un programa en el cual Dados 5 números enteros solicitados al usuario, determinar cuál de los 4 números enteros es más cercano al primero.

numeros=[]

print("Este programa selecciona el valor mas alto de tres numeros.")

numero1=input("Ingrese primer numero: ")

try:
    int(numero1)
except ValueError:
    print("Error! Ingrese un numero entero.")
    exit()
numero1=int(numero1)
numeros.append(numero1)

numero2=input("Ingrese el segundo numero: ")

try:
    int(numero2)
except ValueError:
    print("Error! Ingrese un numero entero.")
    exit()
numero2=int(numero2)
numeros.append(numero2)

numero3=input("Ingrese el tercer numero: ")

try:
    int(numero3)
except ValueError:
    print("Error! Ingrese un numero entero.")
    exit()
numero3=int(numero3)
numeros.append(numero3)

numero4=input("Ingrese el cuarto numero: ")

try:
    int(numero4)
except ValueError:
    print("Error! Ingrese un numero entero.")
    exit()
numero4=int(numero4)
numeros.append(numero4)

numero5=input("Ingrese el quinto numero: ")

try:
    int(numero5)
except ValueError:
    print("Error! Ingrese un numero.")
    exit()
numero5=int(numero5)
numeros.append(numero5)

listaValidacion=[]
cero=abs((numeros[0])-(numeros[1]))
listaValidacion.append(cero)
uno=abs(numeros[0]-numeros[2])
listaValidacion.append(uno)
dos=abs(numeros[0]-numeros[3])
listaValidacion.append(dos)
tres=abs(numeros[0]-numeros[4])
listaValidacion.append(tres)

valorMin=min(listaValidacion)

if valorMin==cero:
    print("El numero mas cercano al {}, es el {}".format((numeros[0]),numeros[1]))
elif valorMin==uno:
    print("El numero mas cercano al {}, es el {}".format((numeros[0]),numeros[2]))
elif valorMin==dos:
    print("El numero mas cercano al {}, es el {}".format((numeros[0]),numeros[3]))
elif valorMin==tres:
    print("El numero mas cercano al {}, es el {}".format((numeros[0]),numeros[4]))
