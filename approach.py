#epsilon
#cuanto mas me aproximo pierdo velocidad.

objetivo  = int(input("Dime un número y te dire la raíz: "))
epsilon   = 0.01
# epsilon   = 0.0001 test para probar rendimiento de epsilon
paso      = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontro la raíz cuadrada {objetivo}")
else:
    print(f"la raíz cuadrada de {objetivo} es {respuesta}")