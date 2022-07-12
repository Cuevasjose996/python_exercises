# Crear un Algoritmo que permita hallar la solución a una ecuación de segundo grado, de la forma: ax^2+bx+c=0
# Los datos del problema son los coeficientes a, b y c. Se desea calcular los valores de x que hacen cierta la ecuación. Dichos valores son:
# ► Consideraciones:
# - En este programa se debe considerar la división por cero que tiene lugar cuando a vale 0 haciendo entonces al denominador, 2a, nulo. Cuando a vale 0 la ecuación no es de segundo grado, sino de primer grado.
# - Otra consideración que debemos tomar en cuenta es que el discriminante (b2- 4ac) no debe ser negativo, de ser negativo la ecuación no tiene soluciones reales.
# Se deben tomar en cuenta los siguientes escenarios:
# 1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
# Si b es DIFERENTE de 0 (b! = 0) la ecuación no tiene solución.
# Se b es IGUAL a 0 (b == 0) se produce la división por cero, y la ecuación tiene infinitas soluciones.
# ► Variables
# a: Coeficiente principal.
# b: Coeficiente secundario.
# c: Término Independiente.
# x1: Incógnita 1.
# x2: Incógnita 2.
# discriminante: Discriminante de la ecuación.
# ► Datos de Prueba.
# a) a = 2 , b = 7, c = 2
# b) a = 1 , b = 2, c = 3
# c) a = 0 , b = 2, c = 3
# d) a = 0 , b = 0, c = 3

Ancho=40
relleno1="-"
relleno2=" "
cadena_vacia=""

mensaje_inicial="ECUACION DE SEGUNDO GRADO: ax^2+bx+c=0"

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

c=input("Ingrese valor de 'c': ")

try:
    int(c)
except ValueError:
    try:
        float(c)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()
c=float(c)

valora=">>> Valor de a: {}".format(a)
valorb=">>> Valor de b: {}".format(b)
valorc=">>> Valor de c: {}".format(c)
ecuacion=("ECUACION: {}x+({})=0".format(b,c))



if a!=0 and 0<((b**2)-(4*a*c)):
    x1=(((-b)+(((b**2)-4*a*c))**(0.5))/(2*a))
    x2=(((-b)-(((b**2)-4*a*c))**(0.5))/(2*a))
    solucion=(">>> SOLUCIONES: x1={} y x2={}".format(x1,x2))
    print(cadena_vacia.center(Ancho,relleno2))
    print(cadena_vacia.center(Ancho,relleno1))
    print(mensaje_inicial.center(Ancho,relleno2))
    print(cadena_vacia.center(Ancho,relleno1))
    print(valora)
    print(valorb)
    print(valorc)
    print(cadena_vacia.center(Ancho,relleno1))
    print(solucion)
    print(cadena_vacia.center(Ancho,relleno1))
elif ((b**2)-(4*a*c))<0:
    solucion=(">>> SOLUCION: No tiene soluciones reales")
    print(cadena_vacia.center(Ancho,relleno2))
    print(cadena_vacia.center(Ancho,relleno1))
    print(mensaje_inicial.center(Ancho,relleno2))
    print(cadena_vacia.center(Ancho,relleno1))
    print(valora)
    print(valorb)
    print(valorc)
    print(cadena_vacia.center(Ancho,relleno1))
    print(solucion)
    print(cadena_vacia.center(Ancho,relleno1))
elif a==0:
    print("La ecuacion es de primer grado!, Respuesta:")
    if b!=0:
        x=-1*(c)/(b)
        if x==-0.0:
            x=0.0
            mensaje_inicial="ECUACION DE PRIMER GRADO: bx+c=0"
            solucion=(">>> SOLUCION: x={}".format(x))
            print(cadena_vacia.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(mensaje_inicial.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(valorb)
            print(valorc)
            print(cadena_vacia.center(Ancho,relleno1))
            print(ecuacion)
            print(cadena_vacia.center(Ancho,relleno1))
            print(solucion)
            print(cadena_vacia.center(Ancho,relleno1))
        else:
            mensaje_inicial="ECUACION DE PRIMER GRADO: bx+c=0"
            solucion=(">>> SOLUCION: x={}".format(x))
            print(cadena_vacia.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(mensaje_inicial.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(valorb)
            print(valorc)
            print(cadena_vacia.center(Ancho,relleno1))
            print(ecuacion)
            print(cadena_vacia.center(Ancho,relleno1))
            print(solucion)
            print(cadena_vacia.center(Ancho,relleno1))
    elif b==0:
        if c!=0:
            mensaje_inicial="ECUACION DE PRIMER GRADO: bx+c=0"
            solucion=">>> SOLUCION: No tiene solucion"
            print(cadena_vacia.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(mensaje_inicial.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(valorb)
            print(valorc)
            print(cadena_vacia.center(Ancho,relleno1))
            print(ecuacion)
            print(cadena_vacia.center(Ancho,relleno1))
            print(solucion)
            print(cadena_vacia.center(Ancho,relleno1))
        if c==0:
            mensaje_inicial="ECUACION DE PRIMER GRADO: bx+c=0"
            solucion=">>> SOLUCION: Tiene infinitas soluciones"
            print(cadena_vacia.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(mensaje_inicial.center(Ancho,relleno2))
            print(cadena_vacia.center(Ancho,relleno1))
            print(valorb)
            print(valorc)
            print(cadena_vacia.center(Ancho,relleno1))
            print(ecuacion)
            print(cadena_vacia.center(Ancho,relleno1))
            print(solucion)
            print(cadena_vacia.center(Ancho,relleno1))
