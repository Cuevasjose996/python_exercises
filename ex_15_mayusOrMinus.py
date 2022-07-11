# Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.

caracter=input("Ingrese una letra: ")

try:
    ord(caracter)
    x=True
except TypeError:
    x=False

mayus=list(range(65,91))
minus=list(range(97,123))

if x==True:
    caracter=ord(caracter)
    if caracter in mayus:
        print("La letra {}, es mayuscula".format(chr(caracter)))
    elif caracter in minus:
        print("La letra {}, es minuscula".format(chr(caracter)))
    else:
        print("Ingrese un caracter valido")
elif x==False:
    print("Error! Ingresa un caracter valido.")