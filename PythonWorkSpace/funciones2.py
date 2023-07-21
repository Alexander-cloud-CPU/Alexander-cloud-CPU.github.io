def adding(a, b, c):#definicion de la funcion
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, c = 1, b = 2)#llamada a la funcion

def introduction(first_name, last_name="Smith"): #definicion de la funcion con valores predeterminados
     print("Hola, mi nombre es", first_name, last_name)

def boring_function():
    return 123
x = boring_function()

def list_sum(lst):#definicion de la funcion con lista
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
print(list_sum([5, 4, 3]))#llamada a la funcion con lista

def strange_list_fun(n):#definicion de la funcion con lista
    strange_list = []#lista vacia
    
    for i in range(0, n):#ciclo for
        strange_list.insert(0, i)#inserta en la lista
    
    return strange_list

print(strange_list_fun(5))#llamada a la funcion con lista