# Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar.


numero=input("Ingrese un numero: ")

try:
    int(numero)
    si=True
except:
    si=False

if si==False:
    print("Error! Ingrese un numero entero.")
elif si==True:
    numero=int(numero)
    if numero%2==0:
        print("el numero {}, es par".format(numero))
    else:
        print("el numero {},es impar".format(numero))
else:
    pass