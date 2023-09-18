def triangulo_rectangulo(numero):
    cadena = ""
    for i in range(1, numero + 1):
        for j in range(i):
            cadena += "*"
        cadena += "\n"
    return cadena


numero = int(input("Ingresa un número entero: "))
triangulo = triangulo_rectangulo(numero)
print(triangulo)
