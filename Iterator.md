Python nos permite realizar iteraciones con el bucle for y while.

al crear una variable que contenga un valor que pueda iterarse:

> > > iter('cadena') # cadena
> > > iter(['a', 'b', 'c']) # lista
> > > iter(('a', 'b', 'c')) # tupla
> > > iter({'a', 'b', 'c'}) # conjunto
> > > iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

podemos usar los bucles para iterarlos.

> > > frutas = ['manzana', 'pera', 'mango']
> > > for fruta in frutas:

        print(fruta)

estudiantes = {
'mexico': 10,
'colombia': 15,
'puerto_rico': 4,
}

for pais in estudiantes:
...

for pais in estudiantes.keys():
...

for numero_de_estudiantes in estudiantes.values():
...

for pais, numero_de_estudiantes in estudiantes.items():
...

tambien podemos usar while para iterar por ejemplo

contenedor = 0

while contenedor < 1:
......contenedor += 1
