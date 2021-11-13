# XCrypt
Modulo con funciones de un cifrado propio que  usa doble cable, una de longitud dinamica a los datos y otra estatica, ambas son necesarias para obetner los datos.
<br>

```
Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import XCrypt
>>> dir(XCrypt)
['__Vpython__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'array_calculo', 'crypt', 'decrypt']

>>> datos = XCrypt.crypt("hola mundo")

>>> datos
{'datos-cifrados': [116883, 109890, 99900, 110889, 0, 0], 'clave-local': [-13, 1, 8, -14, 32, 109], 'clave-secundaria': '-13=h=999=o', 'size': [2, 6], 'array-calculo': {'array': (['h', 'o', 'l', 'a', ' ', 'm'], ['u', 'n', 'd', 'o', '\x00', '\x00']), 'valor-total': 999, 'size': [2, 6]}}

>>> XCrypt.decrypt(datos["datos-cifrados"], datos["clave-secundaria"], datos["clave-local"])
'hola mundo\x00\x00'

>>> 
```
<br>
puedes obtener ayuda del modulo haciendo help(XCrypt).
