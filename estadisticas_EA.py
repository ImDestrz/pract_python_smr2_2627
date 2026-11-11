# Lista de notas
notas = [7, 4, 8, 6, 9, 3, 10]

# Estadísticas
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Suma de las notas:", sum(notas))
print("Cantidad de notas:", len(notas))
print("Nota media:", sum(notas) / len(notas))

# Comprobaciones
print("¿Hay algún suspenso?:", any(nota < 5 for nota in notas))
print("¿No hay ningún cero?:", all(nota != 0 for nota in notas))