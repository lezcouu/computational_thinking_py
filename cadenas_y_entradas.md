Cadenas

Los tipos y significados ayudan a formar cardenas.

> > > 1 + "1"
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: unsupported operand type(s) for +: 'int' and 'str'

> > > 1 \* "1"
> > > '1'

> > > ("Hip " \* 3) + " " +"hurra"
> > > 'Hip Hip Hip hurra'

> > > text = "Text in Python"
> > > len(text)
> > > 14

Posiciones

> > > text[0]
> > > 'T'

> > > text[1]
> > > 'e'

Slice

> > > text[2:]
> > > 'xt in Python'

Obtenemos el texto desde hasta.

> > > text[2: 4]
> > > 'xt'

Texto excepto los ultimos 4 caracteres

> > > text[: -4]
> > > 'Text in Py'

Saltamos de 2 en 2

> > > text[::2]
> > > 'Tx nPto'

> > > f'Yo amo a {text}'
> > > 'Yo amo a Text in Python'

Creamos nuevos espacios en memoria que se apuntan en ese momento.

###Inputs ENTRADADAS

> > > nombre = input("Cual es tu nombre: ")
> > > Cual es tu nombre: Lez
> > > nombre
> > > 'Lez'
> > > print(nombre)
> > > Lez
> > > print("mi nombre es: ", nombre)
> > > mi nombre es: Lez
> > > print("mi nombre es: {nombre}")
> > > mi nombre es: {nombre}
> > > print(f"mi nombre es: {nombre}")
> > > mi nombre es: Lez

> > > numero = input("Escribe un número: ")
> > > Escribe un número: 45
> > > numero
> > > '45'
> > > print(type(numero))
> > > <class 'str'>

> > > numero = int(input("Escribe un número: "))
> > > Escribe un número: 45
> > > numero
> > > 45
> > > print(type(numero))
> > > <class 'int'>
