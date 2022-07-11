#Escribir un programa que pregunte el nombre y apellido del usuario. 
#Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, gusto en conocerte!, donde:

#{nombre} y {apellido} son los valores introducidos.

nombre= input("Como te llamas? ")
apellido= input("Cual es tu apellido? ")

if nombre.isalpha() and apellido.isalpha() == True:
    print("Hola {} {}, gusto de conocerte!".format(nombre,apellido))
else:
    print("Error!, Ingrese nombre y apellidos validos")
