
import random

# Creamos una lista vacía
notas = []

# Generamos 100 notas aleatorias entre 0 y 10
while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

# Contamos cuántos ceros hay en la lista
numCeros = notas.count(0)

print("En mi lista tengo", numCeros, "ceros.")

# Creamos una nueva lista sin los elementos que sean cero
# Solo añadimos las notas diferentes de cero
notas = [nota for nota in notas if nota != 0]

# Mostramos la cantidad de elementos restantes y la lista
print(len(notas), notas)
