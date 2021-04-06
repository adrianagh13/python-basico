# #creación de una función
# def imprimir_mensaje():
#     print('mensaje especial')
#     print('estoy aprendiendo a usar funciones')


# imprimir_mensaje() 
# imprimir_mensaje() 
# imprimir_mensaje() 

def conversacion(mensaje):
    print('hola')
    print('como estás')
    print(mensaje)

opcion  = int(input('Elige una opcion 1 2 o 3 '))
if opcion  == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')
else:
    print('opcion incorrecta')


#Ya no repetimos la misma lógica