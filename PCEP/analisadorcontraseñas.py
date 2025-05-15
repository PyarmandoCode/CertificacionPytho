#Entrada al usuario

password = input("Ingrese una contraseña:")

#1.-Indexing y slicing
#print("\n Primer Caracter:",password[4])
#print("\n Ultimos 3 Caracteres",password[-3:])

#2.-Inmutabilidad (intentar cambiar una letra)
modificada = 'X' + password[1:]
#print("Contraseña modificada (inmutable)" ,modificada)

#3-- Iterar sobre los caracteres
print("\n Caracteres en la contraseña:")
#for c in password:
#    print(c,end="")

#4 Concatenacion y multiplicacion
concatenada= password + "_123"
repetida = password * 2
#print("\n\n Contraseña con sufijo",concatenada)
#print("Contraseña duplicada",repetida)

#5 Comparacion entre strings y numeros (conversion)
if password.isdigit():
    if int(password)>1000:
        print("Numero Mayor que 1000")
    else:
        print("Numero menor o igual a 1000")   
else:
    print("No es un Numero")        