#EJERCICIO 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de 
# cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán 
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el 
# último pedido y calcule el peso total del paquete que será enviado.

muneca = 75
payaso = 112
cantidad_m = int(input('Ingrese la cantidad de muñecas vendidas '))
cantidad_p = int(input('Ingrese la cantidad de payasos vendidos '))
peso_total = muneca * cantidad_m + payaso * cantidad_p
print('El peso total del paquete enviado es ' + str(peso_total) + ' g')

#EJERCICIO 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene 
# un descuento del 60%. Escribir un programa que comience leyendo el número de barras 
# vendidas que no son del día. Después el programa debe mostrar el precio habitual de 
# una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan = 3.49
dcto = .60
barras = int(input('Ingrese la cantidad de barras vendidas que no son del dia '))
total = barras * pan * (1 - dcto)
total = round(total, 2)
print(f'El costo de cada barra es de {pan} y se le hace un descuento del {60}, el total es {total}')




