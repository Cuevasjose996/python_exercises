#Programa que solicite al usuario los datos para calcular el área de un Cuadrado (■), finalmente mostrar el resultado en pantalla.

#► Fórmula: Área del cuadrado

#Area = Lado ** 2

print("-----------------CALCULA EL AREA DE UN CUADRADO-----------------")

valor=input("Cuanto mide un lado: ")


try: 
    float(valor) or int(valor)
    si= True
except ValueError:
    si= False

if si== False:
    print("Error!, ingresa un numero.")
elif si==True:
    valor=float(valor)
    Area=valor**2
    print("El area del cuadrado es: ", Area)