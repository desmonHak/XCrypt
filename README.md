# XCrypt
Modulo con funciones de un cifrado propio que  usa doble cable, una de longitud dinamica a los datos y otra estatica, ambas son necesarias para obetner los datos.
<br>
> python3<br>
Python 3.6.9 (default, Jan 26 2021, 15:33:00) <br>
[GCC 8.4.0] on linux<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
>>> import XCrypt<br>
<br>
>>> dir(XCrypt)<br>
['__Vpython__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'array_calculo', 'crypt', 'decrypt']
<br>
>>> datos = XCrypt.crypt("hola mundo")<br>
>>> <br>
>>> datos<br>
{'datos-cifrados': [116883, 109890, 99900, 110889, 0, 0], 'clave-local': [-13, 1, 8, -14, 32, 109], 'clave-secundaria': '-13=h=999=o', 'size': [2, 6], 'array-calculo': {'array': (['h', 'o', 'l', 'a', ' ', 'm'], ['u', 'n', 'd', 'o', '\x00', '\x00']), 'valor-total': 999, 'size': [2, 6]}}<br>
<br>
>>> XCrypt.decrypt(datos["datos-cifrados"], datos["clave-secundaria"], datos["clave-local"])<br>
'hola mundo\x00\x00'<br>
<br>
>>> 
<br>
