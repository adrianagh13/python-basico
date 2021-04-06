#en python podemos crear una cadena de caracteres de varios renglones con 3 dobles comillas """"""
#para acceder al keyboard de emojis presionamos windows y .
#FUNCIONES EN EL NIVEL SUPERIOR, para que cuando se ejecute el código estén listas las funciones

def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos ' + tipo_pesos + ' tienes? : ')
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares equivalentes a pesos ' + tipo_pesos) 


menu = """
Bienvenido al conversor de monedas 🤑
1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos
Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 20)
else:
    print("Ingrese una opción válida")

# atajo para las triples comillas shift + alt + a
