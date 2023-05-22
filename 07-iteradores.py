lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "PHP", "Ruby", "GO"]

# Iterador
for lenguaje in lenguajes:
    print(f"Estoy aprendiendo {lenguaje}")

# For que escribe numeros
for numero in range(0, 10, 2):
    print(numero)


def iterador(lists):
    print("*----------------------------*")
    for list in lists:
        print(f"Aprendiendo {list}")
    print("*----------------------------*")

iterador(lenguajes)
    