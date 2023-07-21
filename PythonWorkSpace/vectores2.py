my_list = [8, 10, 6, 2, 4]  # lista a ordenar
 
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)        


my_list.sort()#ordenando la lista de menor a mayor
print(my_list) # output: [1, 2, 3, 4, 5]

my_list.reverse()#invierte el orden de la lista de mayor a menor
print(my_list)  # output: [5,4 ,3 ,2 ,1 ]




list_1 = [1]
list_2 = list_1[:]#copiando el contenido de la lista 1 a la lista 2
#list_2 = list_1#copiando la direccion de memoira de la lista 1 a la lista 2
list_1[0] = 2
print(list_2)  # output: [1]

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # Copia elementos desde el índice 1 (incluido) hasta el 3 (excluido).
print(new_list)  # output: [8, 6]

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]#eliminando elementos de la lista
print(my_list)

2 in my_list # verifica si 2 está en la lista
3 not in my_list # verifica si 2 no está en la lista

largest = my_list[0]#inicializando la variable largest con el primer elemento de la lista
for i in range(1, len(my_list)):
    if my_list[i] > largest:#buscando el numero mayor de la lista
        largest = my_list[i]

print(largest)

#buscando un numero  de la lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find #comparando el elemento de la lista con el numero a buscar
    if found:
        break#si lo encuentra sale del bucle
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:#comparando los elementos de la lista bets con los elementos de la lista drawn
    if number in drawn:
        hits += 1
 
print(hits)    