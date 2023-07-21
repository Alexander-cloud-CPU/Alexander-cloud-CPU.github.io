# asi se hacen comentarios
x = int(input("Ingrese un numero: "))
j = input("Ingrese una plabra: ")
print("Su palabra es", j, "\nSu numero es", x, sep=":", end="")

if x >= 10:
    print("Su numero es mayor o igual a 10")
else:
    print("Su numero es menor a 10")