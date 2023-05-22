lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

print(lenguajes)

# Los arrays (lists) comienzan en la posicion 0
print(lenguajes[0]) # Python

# Ordenar los elementos
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}"
print(aprendiendo)

# Modificando arreglo
lenguajes[2] = "PHP"
print(lenguajes)

# Agregar elementos a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

# Eliminar de un arreglo (list)
lenguajes.pop() # Eliminar el ultimo elemento
print(lenguajes)

# Eliminar con pop una pocision en especifico
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)