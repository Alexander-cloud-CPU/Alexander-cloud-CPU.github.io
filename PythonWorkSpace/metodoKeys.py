dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():#imprime las claves del diccionario
    print(key, "->", dictionary[key])

#Otra manera de hacerlo es utilizar el método items(). Este método retorna una lista de tuplas (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)    

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)

#FUNCION SORTED 
#La función sorted() acepta cualquier secuencia (lista, tupla, cadena) como argumento, y regresa una lista como resultado.
#for key in sorted(dictionary.keys()):

#FUNCION VALUE
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for french in dictionary.values():
    print(french)


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)#cuenta cuantas veces se repite el numero 2

print(duplicates)     