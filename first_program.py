def first_program():
    nombre = input("¿Podrias decirme cual es tu nombre?, yo te dire cuantas letras contiene: ")

    print(f"tu nombre contiene {len(nombre)} letras.")

first_program()

def read():
    consulta = input("¿Quieres que te lea un chiste? Si/No: ")

    if consulta == "Si":
        print("¿Por qué los pajaros no usan Facebook?, porque tienen twitter")
    else:
        print("Que aburrido bueno.")

read()