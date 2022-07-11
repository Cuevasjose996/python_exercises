# Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius.

# ► Fórmula: Grados Farenheit a Grados Celcius

# celcius = (fahrenheit - 32.0) * 5.0 / 9.0


print("-----------------CALCULA LA CONVERSION DE TEMPERATURA-----------------")

farenheit=input("Ingrese grados celsius: ")

try: 
    float(farenheit) 
    si= True
except ValueError:
    si= False

if si== False:
    print("Error!, ingresa un numero.")
elif si==True:
    farenheit=float(farenheit)
    celcius=(farenheit-32)*1.8
    print("El resultado es: \n{} grados farenheit={} grados celcius".format(farenheit,celcius))