# Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado, de la forma: ax + b = 0
# El objetivo es despejar la x y validar los posibles datos para arrojar la respuesta.
# Al despejar la x tendremos que:
# x = -b/a
# Por lo tanto tendremos los siguientes escenarios:
# 1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
# 2) Si a es IGUAL a 0 (a == 0) tendremos que:
# Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.
# Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones
# ► Variables:
# a: Coeficiente principal.
# b: Término Independiente.
# x: Incógnita.
# ► Datos de Prueba.
# a) a = 2 y b = 6.
# b) a = 0 y b = 3.
# c) a = 0 y b = 0.

Ancho=40
relleno1="-"
relleno2=" "
cadena_vacia=""

mensaje_inicial="ECUACION DE PRIMER GRADO: ax+b=0"

a=input("Ingrese valor de 'a': ")

try:
    int(a)
except ValueError:
    try:
        float(a)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()
a=float(a)
b=input("Ingrese valor de 'b': ")

try:
    int(b)
except ValueError:
    try:
        float(b)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()
b=float(b)

valora=">>> Valor de a: {}".format(a)
valorb=">>> Valor de b: {}".format(b)
ecuacion=("ECUACION: {}x+({})=0".format(a,b))



if a!=0:
    x=-1*(b)/(a)
    if x==-0.0:
        x=0.05
        solucion=(">>> SOLUCION: x={}".format(x))
        print(cadena_vacia.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(mensaje_inicial.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(valora)
        print(valorb)
        print(cadena_vacia.center(Ancho,relleno1))
        print(ecuacion)
        print(cadena_vacia.center(Ancho,relleno1))
        print(solucion)
        print(cadena_vacia.center(Ancho,relleno1))
    else:
        solucion=(">>> SOLUCION: x={}".format(x))
        print(cadena_vacia.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(mensaje_inicial.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(valora)
        print(valorb)
        print(cadena_vacia.center(Ancho,relleno1))
        print(ecuacion)
        print(cadena_vacia.center(Ancho,relleno1))
        print(solucion)
        print(cadena_vacia.center(Ancho,relleno1))
elif a==0:
    if b!=0:
        solucion=">>> SOLUCION: La ecuacion no tiene solucion"
        print(cadena_vacia.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(mensaje_inicial.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(valora)
        print(valorb)
        print(cadena_vacia.center(Ancho,relleno1))
        print(ecuacion)
        print(cadena_vacia.center(Ancho,relleno1))
        print(solucion)
        print(cadena_vacia.center(Ancho,relleno1))
    if b==0:
        solucion=">>> SOLUCION: Tiene infinitas soluciones"
        print(cadena_vacia.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(mensaje_inicial.center(Ancho,relleno2))
        print(cadena_vacia.center(Ancho,relleno1))
        print(valora)
        print(valorb)
        print(cadena_vacia.center(Ancho,relleno1))
        print(ecuacion)
        print(cadena_vacia.center(Ancho,relleno1))
        print(solucion)
        print(cadena_vacia.center(Ancho,relleno1))