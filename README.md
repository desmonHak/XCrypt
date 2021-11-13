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
Esta es la ayuda que ofrece el modulo haciendo help(XCrypt).
```
Help on module XCrypt:

NAME
    XCrypt - --- algortimo de cifrado  de doble clave ---

DESCRIPTION
    Modulo para cifrado de datos. Generando claves unicas
    para la descompresion de los datos.

FUNCTIONS
    array_calculo(texto)
        Esta funcion se usa para calcular el array bidimensional y 
        otorgar los valores dentro de ellos, tambien calculo otro tipo
        de datos.
        ---------------------------
        input  = texto(string)
        ===========================
        output = arr(dicionario)
        ---------------------------
        
        El dicionario de salida tiene la siguiente estructura:
        arr = {
                "array" : ( list(), list() ),
                "valor-total":0,
                "size" : [2, 0]
        }
    
    crypt(texto)
        Esta funcion es la encargada de codificar los datos.
        -----------------------------
        Input = texto(string)
        =============================
        Output = output(dicionario)
        -----------------------------
        El dicionario de salida tiene la siguiente forma:
        
        output = {
                "datos-cifrados": list(),
                "clave-local": list(),
                "clave-secundaria" : str(),
                "size": arr["size"],
                "array-calculo":arr
        }
    
    decrypt(datos_cifrados, clave_secundaria, clave_local)
        Se usa para descodificar los datos.
        --------------------------------------------------------
        Input = datos_cifrados(lista), clave_secundaria(string), 
                clave_local(lista)
        ========================================================
        Output = texto(string)
        ---------------------------------------------------------

DATA
    __Vpython__ = 2.17

VERSION
    1.0

AUTHOR
    Desmon

FILE
    /home/kodachi/Desktop/XCrypt.py

```
