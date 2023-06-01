def first_program():
    nombre = input("¿Podrias decirme cual es tu nombre?, yo te dire cuantas letras contiene: ")

    print(f"tu nombre contiene {len(nombre)} letras.")

# first_program()

def read():
    consulta = input("¿Quieres que te lea un chiste? Si/No: ")

    if consulta == "Si":
        print("¿Por qué los pajaros no usan Facebook?, porque tienen twitter")
    else:
        print("Que aburrido bueno.")

# read()

def write_a_number():
    number = int(input("Escribe un número: "))
    print(f"El número que escribiste es {number}")
    print(f"Ademas te cuento que tu número es de tipo {type(number)}")

# write_a_number()

def less_number(name):
    print(f"El número que estoy pensando es mayor a tu número elegido.")
    other_number = input("¿Quieres intentar otro número? Si/No ")
    if other_number == "Si":
        what_is_your_number(name)
    if other_number != "Si":
        print(f"Gracias, Adios!")

def greather_number(name):
    print(f"El número que estoy pensando es menor a tu número elegido.")
    other_number = input("¿Quieres intentar otro número? Si/No ")
    if other_number == "Si":
        what_is_your_number(name)
    if other_number != "Si":
        print(f"Gracias, Adios!")

def what_is_your_number(name):
    number = int(input(f"{name} Juguemos, Dime un número y te dire si es mayor o menor al que pienso: "))
    if number == 2:
        print(f"Acertaste 2 es el número que yo estaba pensando.")
    if number < 2:
        less_number(name)
    if number > 3:
        greather_number(name)


def play_with_operators():
    name   = input("Hola!, ¿Cuál es tu nombre?: ")
    what_is_your_number(name)

play_with_operators()