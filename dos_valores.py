# Se trata de tomar una lista de los valores desordenados 
# y producir una salida en orden creciente.

n = [15, 23]
if n[0] > n[1]:
    a = n[0]
    n[0] = n[1]
    n[1] = a
print (n)