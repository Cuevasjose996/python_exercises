# Crea una matriz 3x3 que almacene los valores del 1 al 9. El tamaño de la matriz indica la cantidad de filas. Imprime cada fila de la matriz en pantalla.

array=[[1,2,3],[4,5,6],[7,8,9]]

longitud=len(array)

print(">>>IMPRIMIR MATRIZ : ",array)

for fila in range(longitud):
    print(">>>FILA %d : %s" %(fila+1,array[fila]))