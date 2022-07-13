# Haz un programa para crear una matriz nula Mmxn, 
# donde se le solicite al usuario su dimensión m x n, (m son las filas y n son las columnas). 
# Imprime cada fila de la matriz en pantalla.

from numpy import array


filas=input("Ingresa el numero de filas: ")

try:
    int(filas)
except ValueError:
    print("Error! Ingrese valores enteros")
    exit()

filas=int(filas)

columnas=input("Ingresa el numero de columnas: ")

try:
    int(columnas)
except ValueError:
    print("Error! Ingrese valores enteros")
    exit()

columnas=int(columnas)
matrizNula=[]

for f in range(filas):
    matrizNula.append([0]*columnas)    

print(">>> MATRIZ M ({}x{}): ".format(filas,columnas), matrizNula)
for valor in range (filas):
    print(matrizNula[columnas])