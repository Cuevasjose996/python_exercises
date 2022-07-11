# Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.

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
    if numero%3==0:
        print("el numero {}, es multiplo de 3".format(numero))
    else:
        print("el numero {}, no es multiplo de 3".format(numero))
else:
    pass