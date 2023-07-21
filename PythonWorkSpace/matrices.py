row = [8 for i in range(8)]#creando una fila de 8 elementos 8 es los elementos que llenaran la fila y range( es la cantidad de elementos)



temps = [[0.0 for h in range(24)] for d in range(31)] #creando una matriz de 31 filas y 24 columnas llena de 0.0
print(temps)

temps[0][0] = 1.0 #asignando un valor a la fila 0 columna 0


hot_days = 0
 
for day in temps:#recorriendo la matriz
    for temp in day:#recorriendo la fila
        if temp > highest:#buscando el numero mayor de la fila
            highest = temp #asignando el numero mayor a la variable highest
 
print("La temperatura más alta fue:", highest)


for day in temps:#recorriendo la matriz
    if day[11] > 20.0:#buscando el numero mayor de la fila
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)
 
table = [[":(", ":)", ":(", ":)"], #fila 0
         [":)", ":(", ":)", ":)"], #fila 1
         [":(", ":)", ":)", ":("], #fila 2
         [":)", ":)", ":)", ":("]] #fila 3
 
print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)