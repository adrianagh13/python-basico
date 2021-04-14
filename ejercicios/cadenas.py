# EJERCICIO 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
# nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir 
# su nombre combinando mayúsculas y minúsculas como quiera.

# nombre = input('Ingrese su nombre ')

# print(nombre.lower())
# print(nombre.upper())
# print(nombre.capitalize())

#Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
# muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> 
# es el número de letras que tienen el nombre.

# nombre = input('Ingrese su nombre')
# num = len(nombre)
# print(f'Su nombre: {nombre} tiene {num} letras')

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código 
# del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte 
# por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

# numero_telefono = input('Ingrese un numero telefonico con el prefijo y extensión del mismo ')
# numero = numero_telefono[2:12]
# print('El numero de telefono sin prefijo y extension es ' + numero )

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla 
# la frase invertida.
# frase = input('Ingrese una frase ')
# print('Frase invertida ' + frase[::-1])

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por 
# pantalla la misma frase pero con la vocal introducida en mayúscula.
# frase = input('Ingrese una frase ')
# vocal = input('Ingrese la vocal a modificar ')
# frase = frase.replace(vocal, vocal.upper())
# print('Frase con vocal modificada ' + frase)

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo 
# electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

email = input('Ingrese el correo electrónico ')
print(email[:email.find('@')] + '@ceu.es')
