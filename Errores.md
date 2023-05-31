#Elementos básicos

#Pruebas con consola

#<literales> = 1, "abc", 2.0, True
#<operadores> = + / * % ** = ==
#<literal> <operador> <literal>
>>> 1+1
2

>>> 1 3.9
  File "<stdin>", line 1
    1 3.9
      ^^^
SyntaxError: invalid syntax

>>> 5/ "Platzi"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'int' and 'str'

>>> 5 * "Platzi"
'PlatziPlatziPlatziPlatziPlatzi'

>>> print("Hola, mundo!")
Hola, mundo!
