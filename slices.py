nombre = 'Adriana'
#Imprime los caracteres desde la posición 0 hasta antes de la 3
print(nombre[0:3])
#Toma por defecto la posición 0 si la obviamos
print(nombre[:3]) 
#Puede tomar por defecto todos los caracteres
print(nombre[::])
#El tercer parámetro son los saltos o recorrido entre caracteres
print(nombre[1:6:2])
#Si el tercer parámetro es negativo comienza los saltos desde la última posición, 
print(nombre[::-1])