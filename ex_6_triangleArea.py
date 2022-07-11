# Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), finalmente mostrar el resultado en pantalla.

# ► Fórmula: Área del Triángulo

# Area = (Base*Altura)/2



print("-----------------CALCULA EL AREA DE UN TRIANGULO-----------------")

base=input("Cuanto mide la base: ")
altura=input("Cuanto mide la altura:")



try: 
    float(base) 
    float(altura)
    si= True
except ValueError:
    si= False

if si== False:
    print("Error!, ingresa un numeros.")
elif si==True:
    base=float(base)
    altura=float(altura)
    Area=(base*altura)/2
    print("El area del triangulo es: ", Area)