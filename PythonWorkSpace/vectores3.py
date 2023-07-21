my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = [my_list[0]]
for i in range(len(my_list)):#recorriendo la lista
    if my_list[i] not in new_list:#verificando si el elemento de la lista no esta en la nueva lista
        new_list.append(my_list[i])#agregando el elemento a la nueva lista

            
print("La lista con elementos únicos:")
print(new_list)