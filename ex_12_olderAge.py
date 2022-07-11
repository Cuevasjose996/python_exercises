# Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor. Ejemplo:

# - La Primera persona es mayor!

# Si la edad de ambos es igual se muestra el siguiente mensaje:

# - Ambos tienen la misma edad!


edad1=input("Ingrese la primera edad: ")
edad2=input("Ingrese la segunda edad: ")

try: 
    int(edad1)
    int(edad2) 
    si= True
except ValueError:
    si= False

if si==False:
    print("Error! Ingrese valores numericos enteros.")
elif si==True:
    edad1=int(edad1)
    edad2=int(edad2)
    if 0<=edad1 and 0<=edad2 and edad2 < edad1:
        print("La primera persona es mayor!")
    elif 0<=edad1 and 0<=edad2 and edad1<edad2:
        print("La segunda persona es mayor!")
    elif 0<=edad1 and 0<=edad2 and edad1==edad2:
        print("Ambos tienen la misma edad!")
    else: 
        print("Error! Ingrese valores validos")
