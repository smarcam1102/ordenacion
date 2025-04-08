# Archivo: tres_valores.property.py 
# Fecha: 08/04/25
# Proy.: estudio de algoritmos
#
# Ordenar crecientemente una lista de tres valores
# Existe un error, ya que según los valores, puede cambiar
# dos que entre ellos había que cambiar, pero genera mal orden
# en los posteriores

# Función swap (int indice)
# cambia de orden dos elementos de una lista ya existente s
# 
def swap(indice):
    a = s[indice]
    s[indice] = s[indice]
    s[indice] = a 


n = []

# Bucle para tomar datos del teclado y guardarlos en la variable n de tipo lista
for i in range(3):
    n.append(int(input())) # append es un método de las listas

s = n # Voy a hacer dos intentos de ordenar. Para tener 
      # la lista original sin cambios, tendré que copiarla a otra lista
      # y así trabajamos con la copia

for i in range(5):   # Aquí se refelja el error p.ej. con
    if s[i] > s[i+1]:
        a = s[i]
        s[i] = s[i+1]
        s[i+1] = a
print(s)

s = n
for i in range(len(n)-2):     #Aquí hacemos el repaso a la lista dos veces 
    for j in range (len(n)-1):
        if s[j] > s[j+1]:
            swap(j)
print(s)

