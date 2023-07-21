numbers = [10, 5, 7, 2, 1]

vector = [1, None, True, 'Soy una cadena', 256, 0]#lista con diferentes tipos de datos
print(vector[3])  # output: Soy una caden
print(vector[-1])  # output: 0

print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111#modificando el primer elemento de la lista
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual
print(numbers[3]) # Accediendo al primer elemento de la lista.
print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.
del numbers[1]# Eliminando el segundo elemento de la lista.
print(len(numbers))# Imprimiendo la longitud de la lista.
print(numbers)

print(numbers[-1])# Imprimiendo el último elemento de la lista.
print(numbers[-2])# Imprimiendo el penúltimo elemento de la lista.

#list.append(value)
# realiza mediante un método llamado append(). Toma el valor de su argumento y lo coloca al final de la lista que posee el método.
#La longitud de la lista aumenta en uno.
numbers.append(4)
print(len(numbers))
print(numbers)


#list.insert(location, value)
#El método insert() es un poco más inteligente - puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.
numbers.insert(0, 222)#el 0 es la posicion donde inserta 222
print(len(numbers))
print(numbers)

my_list = []  # Creando una lista vacía.

for i in range(5):#dando valores a la lista con append
    my_list.append(i + 1)

print(my_list)

my_list = []  # Creando una lista vacía.
 
for i in range(5):#dando valores a la lista con insert
    my_list.insert(0, i + 1)
print(my_list)

total = 0
for i in my_list:#sumando los valores de la lista y recooriendo la lista
    total += i
print(total)

for i in range(len(my_list) // 2):#intercambiando valores de la lista
    my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]#my_list[len(my_list) - i - 1] es el ultimo de la lista
print(my_list)
