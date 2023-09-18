# Crear un conjunto utilizando llaves
frutas = {'manzana', 'plátano', 'naranja', 'manzana', 'mango'}

# Crear un conjunto utilizando la función set()
colores = set(['rojo', 'verde', 'azul', 'verde'])

print(frutas)  # Salida: {'naranja', 'plátano', 'manzana', 'mango'}
print(colores) # Salida: {'verde', 'rojo', 'azul'}

# Operaciones de conjuntos
frutas.add('kiwi')
colores.remove('verde')

print(frutas)  # Salida: {'naranja', 'plátano', 'kiwi', 'manzana', 'mango'}
print(colores) # Salida: {'rojo', 'azul'}

# Comprobación de pertenencia
if 'naranja' in frutas:
    print("Sí, hay una naranja en el conjunto de frutas.")

# Operaciones de conjuntos (unión e intersección)
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

union = conjunto1.union(conjunto2)
interseccion = conjunto1.intersection(conjunto2)

print(union)         # Salida: {1, 2, 3, 4, 5, 6}
print(interseccion)  # Salida: {3, 4}