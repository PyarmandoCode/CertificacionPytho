"""
.isalpha() .- Verifica si solo son letras
.isdigit() .- Verifica si solo son digitos
.islower() .- Verifica si son Minusculas
.isupper() .- Verifica si son Mayusculas
.isspace() .- Verifica si solo son espacios en Blanco
Vericar si una cadena cumple una condicion especifica
.join().-.Une Elementos de un iterable (lista) en una sola cadena
usando el string como separador
.split().-Divide una cadena en partes usando el separador (sep) devuelve una lista
.sort():- Ordena una lista modificando la lista de origen (in-place)
.sorted(iterable).-Devuelve una nueva lista ordenada sin modificar el original
.index(valor) .- Devuelve la posicion de la primera apracio del valor .Si no lo encuentra lanza un error
.find(valor) .-Similar a index pero devuelve -1 si no lo encuentra
.rfind(valor) .-Busca el valor desde el final hacia el principio devuelve la ultima posicion o -1 si no lo encuentra
"""

texto="Python"
documento="123456"
frase="PYTHON ES FACIL DE APRENDER"
espacio="  "
#print(texto.isalpha()) #True
#print(documento.isdigit()) #False
#print(frase.isupper())
#print(espacio.isspace())

palabras=["Hola","mundo","Python"]
frase=" ".join(palabras)
#print(frase)

frase="Hola Mundo Python"
palabras=frase.split(" ")
#print(palabras)

nombres=["Juan","Ana","Pedro"]
nombres.sort()
#print(nombres)

numeros=[3,1,4,2]
ordenados=sorted(numeros)
#print(ordenados)
#print(numeros) #Original no cambia

texto="programacion"
#print(texto.find("h"))

texto="banana"
print(texto.rfind("a"))

