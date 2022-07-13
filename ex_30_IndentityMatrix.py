# Haz un programa que pida un entero positivo n y 
# almacene en una variable M la matriz identidad de n × n (la que tiene unos (1) en la diagonal principal y ceros (0) en el resto de celdas). 
# Imprime la matriz en pantalla.



dimension=input("Ingresa la dimension de la matriz: ")

try:
    int(dimension)
except ValueError:
    print("Error! Ingrese valores enteros")
    exit()

dimension=int(dimension)
filas=int(dimension)
columnas=int(dimension)
matrizNula=[]

for f in range(dimension):
    matrizNula.append([0]*dimension)    

for f in range(dimension):
    for c in range(dimension):
        if f==c:
            matrizNula[f][c]=1

print(">>> MATRIZ M ({}x{}): ".format(filas,columnas), matrizNula)

for valor in range(dimension):
    print(matrizNula[valor])