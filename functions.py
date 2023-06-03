#touring complete con las variables. comenzamos parte2 modulo 4.

#vamos a conocer funciones y alcance de las funciones.

#Abstracción

#  Poder separar el código de su uso. 

#Decomposición.

#  Abstraer mini programas dentro de un programa mayor. 

# def <nombre>(<parametros>):
#     <cuerpo>
#     return <expresion>

# invocacion(param1, param2)

# def suma(a,b):
#     total = a + b
#     return total

# suma(2,3)


#Argumentos keyword y valores por defecto


# def nombre_completo(nombre, apellido, inverso=False):
#     if inverso:
#         return f"{apellido} {nombre}"
#     else:
#         return f"{nombre} {apellido}"

# nombre_completo("David", "Aroesti") sin nombrar.
# nombre_completo("David", "Aroesti", inverso=True) por posicion y nombramos la que queremos.
# nombre_completo(nombre="David", apellido="Aroesti") nombradas.


#Reto crear un algoritmo e incapsularlo para su uso.

#epsilon
#cuanto mas me aproximo pierdo velocidad.

def normal_search(objetivo):
    epsilon   = 0.01
# epsilon   = 0.0001 test para probar rendimiento de epsilon
    paso      = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return(f"No se encontro la raíz cuadrada {objetivo}")
    else:
        return(f"la raíz cuadrada de {objetivo} es {respuesta}")

def binary_search(objetivo):
    epsilon   = 0.0001
    bajo      = 0.0
    alto      = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

# Al realizar una busqueda binaria.
# Es mas fácil encontrar nuestra raíz mas facilmente.
# Aunque nuestro epsilon sea mas preciso que 0.01
# Solo sirve para buscar dentro de un conjunto ordenado.

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return f"La raíz cuadrada de {objetivo} es {respuesta}"

def search_square_root(choice, objetivo):
    functions_search = {
        "a": binary_search,
        "b": normal_search
    }
    selected_search = functions_search.get(choice)
    result = selected_search(objetivo)
    return result

def type_of_search(objetivo):
    choice = input("¿Quieres realizar una busqueda A)binaria o B)normal? responde por favor A o B: ")
    if choice.lower() == "a" or choice.lower() == "b":
        return search_square_root(choice, objetivo)
    else:
        type_of_search(objetivo)

def tell_me_a_number():
    objetivo  = int(input("Dime un número y te dire su raíz: "))
    if isinstance(objetivo, int) or isinstance(objetivo, float):
        return objetivo
    else:
        tell_me_a_number()

def what_is_your_root():
    objetivo = tell_me_a_number()
    result = type_of_search(objetivo)
    print(result)

what_is_your_root()