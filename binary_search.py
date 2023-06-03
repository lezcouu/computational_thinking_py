objetivo  = int(input("Escoge un número: "))
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

print(f"La raíz cuadrada de {objetivo} es {respuesta}")