secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
x = int(input())
while x != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    x = int(input("Ingresa otro numero: "))
        
print("\n",x)       
print("¡Bien hecho, muggle! Eres libre ahora.") 