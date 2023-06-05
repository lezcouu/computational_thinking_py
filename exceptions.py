"""
Manejo de excepciones
- No existen excepciones.
- La mayoria son errores de semántica

python      => try, except, finally
javascript  => try, catch, finally

para tirar la excepcion keyword raise
"""

def divide_elements_of_list(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list

lista   = list(range(10))
divisor = 0

print(divide_elements_of_list(lista, divisor))