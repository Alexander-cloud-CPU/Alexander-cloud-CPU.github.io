#cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, o cualquier otro tipo de dato).
tuple_1 = (1, 2, 4, 8)#tupla de enteros
empty_tuple = ()#tupla vacia
tuple_2 = 1., .5, .25, .125#tupla de punto flotante
one_element_tuple_1 = (1, )#tupla de un elemento
one_element_tuple_2 = 1.,#tupla de un elemento
 
print(tuple_1)
print(tuple_2)

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])#imprime el primer elemento de la tupla
print(my_tuple[-1])#imprime el ultimo elemento de la tupla
print(my_tuple[1:])#imprime desde el segundo elemento hasta el final de la tupla
print(my_tuple[:-2])#imprime desde el primer elemento hasta el penultimo elemento de la tupla

for elem in my_tuple:#imprime cada elemento de la tupla
    print(elem)

#la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
#el operador + puede unir tuplas (ya se ha mostrado esto antes)
#el operador * puede multiplicar las tuplas, así como las listas;
#los operadores in y not in funcionan de la misma manera que en las listas.   

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))#imprime el numero de elementos de la tupla
print(t1)#imprime la tupla t1
print(t2)#imprime la tupla t2
print(10 in my_tuple)#imprime True si el elemento 10 esta en la tupla
print(-10 not in my_tuple)#imprime True si el elemento -10 no esta en la tupla  