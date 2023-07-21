#for i in range(100):
    # do_something()
#    pass

#CON UN ARGUMENTO
#por defecto i vale 0
for i in range(10):
    print("El valor de i es", i)
    if i == 9:
        print("\n")

#CON DOS ARGUMENTOS
# el 2 es el valor con el que inicia i, y 8 el valor donde acaba el bucle
#range solo acepta enteros como argumento
for i in range(2, 8):
    print("El valor de i es", i)
    if i == 6:
        print("\n")
  
#CON TRES ARGUMENTOS
# el 3 es la cantidad en la que i va ir aumentando
for i in range(2, 8, 3):
    print("El valor de i es", i)


