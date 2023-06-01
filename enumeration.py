#Enumeración exhaustiva
#- "Adivina y verifica"
#- "Pc actuales muy rapidas"
#- "Primer algoritmo a conocer"

# def what_is_you_root():
objetivo = int(input("Escoge un número entero: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f"La raiz cuadrada de {objetivo} es {respuesta}")
else:
    print(f"{objetivo} no tiene una raíz cuadrada exacta.")

# what_is_you_root()