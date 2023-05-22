nombre = "Pedro"

# Sintaxis para definir una funcion
def mostrar_nombre(nombre):
    print(f"Hola soy {nombre}")

mostrar_nombre(nombre)

# Sintaxis para un metodo
print(nombre.upper())

# Reto de la seccion
def welcome():
    print("Bienvenido")

welcome()

def welcome_user(username):
    print(f"Welcome user {username}")

welcome_user("JuanF31")

def last_activity(activity):
    return activity

last = last_activity("Learning Python")
print(last)