#voy a trabajar en consola y poner algunos ejemplos de diccionarios.

"""
Estructura de datos
>>> my_dict = {
...     'David': 35,
...     'Erika': 32,
...     'Jaime': 50
... }
>>>
>>> my_dict
{'David': 35, 'Erika': 32, 'Jaime': 50}
>>> my_dict["Erick"
... ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Erick'
>>> my_dict.get("juan")
>>> my_dict.get("juan",30)
30
>>> my_dict.get("David",30)
35
>>> my_dict["Jaime"] = 20
>>> my_dict
{'David': 35, 'Erika': 32, 'Jaime': 20}
>>> my_dict["Juan"] = 19
>>> my_dict
{'David': 35, 'Erika': 32, 'Jaime': 20, 'Juan': 19}
>>> del my_dict["Erika"]
>>> my_dict
{'David': 35, 'Jaime': 20, 'Juan': 19}
>>> 
"""


"""Aprendiendo a iterare
>>> for llave in my_dict.keys():
...     print(llave)
... 
David
Jaime
Juan
>>> for llave in my_dict.values():
...     print(llave)
... 
35
20
19
>>> for llave in my_dict.items():
...     print(llave)
... 
('David', 35)
('Jaime', 20)
('Juan', 19)
>>>
"""

"""Averiguar si existe mi valor
>>> "Juan" in my_dict
True
>>> "Pablo" in my_dict
False
>>>
"""

"""Creamos un nuevo dictionary comprehension es util para evitar hacer loops y
transformar nuestros datos de otra forma
>>> dict_comprehension["1"] = 1
>>> dict_comprehension["2"] = 2
>>> new_dict_comprehension = {n: n*2 for n in dict_comprehension}
>>> new_dict_comprehension
{'1': '11', '2': '22'}
"""