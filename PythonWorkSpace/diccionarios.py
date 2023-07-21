#El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"} #diccionario ingles-frances
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}#diccionario de numeros de telefono
empty_dictionary = {}#diccionario vacio
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
#En el mundo de Python, la palabra que se esta buscando se denomina key. La palabra que se obtiene del diccionario es denominada value.
#la función len() aplica también para los diccionarios - regresa la cantidad de pares (clave-valor) en el diccionario;

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary["gato"])#imprime el valor de la clave "gato"

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:#si la palabra esta en el diccionario
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}



