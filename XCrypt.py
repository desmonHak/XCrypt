
__doc__ = """
	--- algortimo de cifrado  de doble clave ---

	Modulo para cifrado de datos. Generando claves unicas
	para la descompresion de los datos.

"""

__author__  = "Desmon"
__version__ = 1.0
__Vpython__  = 2.17

def array_calculo(texto):
	"""
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

	"""

	longitud = len(texto)+1
	arr = {
		"array" : ( list(), list() ),
		"valor-total":0,
		"size" : [2, 0]
	}

	longitud_sin_espacios = 0
	columna_array = 0
	contador = 0


	for txt in texto:
		longitud_sin_espacios += len(txt)
		arr["valor-total"] += ord(txt)

	for txt in texto:
		if longitud / 2 <= contador: columna_array = 1
		else: columna_array = 0

		for letter in txt: arr["array"][columna_array].append(letter)
		contador+=1

	if len(arr["array"][0]) > len(arr["array"][1]):
		for i in range(len(arr["array"][0]) - len(arr["array"][1])): arr["array"][1].append("\0")
	elif len(arr["array"][0]) < len(arr["array"][1]):
		for i in range(len(arr["array"][1]) - len(arr["array"][0])): arr["array"][1].append("\0")
	#else: raise Exception("[!] Algo extrano paso en el proceso")

	if len(arr["array"][0]) ==  len(arr["array"][1]) and arr["valor-total"] <= 1114111:
		arr["size"][1] = len(arr["array"][0])
		return arr

	else: raise Exception("[!] Algo extrano paso en el proceso")

def crypt(texto):
	"""
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

	"""

	if type(texto) != type(""):
		return -1
	if len(texto) == 0:
		return -1

	arr = array_calculo(texto)

	output = {
		"datos-cifrados": list(),
		"clave-local": list(),
		"clave-secundaria" : str(),
		"size": arr["size"],
		"array-calculo":arr
	}
	

	
	for i in range(len(arr["array"][0])):
		valor = 0
		valor = ord(arr["array"][0][i]) - ord(arr["array"][1][i])

		output["clave-local"].append(valor)
		output["datos-cifrados"].append(ord(arr["array"][1][i])*arr["valor-total"])
		
	output["clave-secundaria"] += str(output["clave-local"][0])
	output["clave-secundaria"] += "="
	output["clave-secundaria"] += texto[0]
	output["clave-secundaria"] += "="
	output["clave-secundaria"] += str(arr["valor-total"])
	output["clave-secundaria"] += "="
	output["clave-secundaria"] += texto[len(texto)-1]
	
	
	return output
	
def decrypt(datos_cifrados, clave_secundaria, clave_local):
	"""
	Se usa para descodificar los datos.
	--------------------------------------------------------
	Input = datos_cifrados(lista), clave_secundaria(string), 
		clave_local(lista)
	========================================================
	Output = texto(string)
	---------------------------------------------------------
	"""

	if type(datos_cifrados)   != type([]) or \
	   type(clave_secundaria) != type("") or \
	   type(clave_local)      != type([]):
		return -1

	texto = [[],[]]
	factor_exponencial = int(clave_secundaria.split("=")[2])
	for i in range(len(datos_cifrados)):
		datos_cifrados[i] = datos_cifrados[i] / factor_exponencial

		texto[0].append(chr(int(datos_cifrados[i] + (clave_local[i]))))
		texto[1].append(chr(int(datos_cifrados[i])))

	texto = "".join(texto[0]) + "".join(texto[1])
	
	return texto

if __name__ == "__main__":

	from getpass import _raw_input

	datos = crypt(_raw_input("text: "))

	print(datos)
	print("\n")

	print("Datos cifrados: "+"=".join(str(elem) for elem in datos["datos-cifrados"]))

	print("Clave local: "+"=".join(str(elem) for elem in datos["clave-local"]))

	print("Clave secundaria: "+datos["clave-secundaria"])

	print(decrypt(datos["datos-cifrados"], datos["clave-secundaria"], datos["clave-local"]))
