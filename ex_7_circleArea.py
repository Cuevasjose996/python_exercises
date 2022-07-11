# Programa que solicite al usuario los datos para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla.

# ► Fórmula: Área del Círculo

# Area = PI*(Radio**2)
import math

print("-----------------CALCULA EL AREA DE UN CIRCULO-----------------")

radio=input("Cuanto mide el radio: ")

try: 
    float(radio) 
    si= True
except ValueError:
    si= False

if si== False:
    print("Error!, ingresa un numeros.")
elif si==True:
    radio=float(radio)
    Area=math.pi*(radio**2)
    print("El area del circulo es: ", round(Area,2))