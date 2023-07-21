def my_function():
    global var#global es para que la variable sea global
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)


def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # probando
    print(n, factorial_function(n))

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)