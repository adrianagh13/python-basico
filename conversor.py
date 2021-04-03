#en python podemos crear una cadena de caracteres de varios renglones con 3 dobles comillas """"""
#para acceder al keyboard de emojis presionamos windows y .

menu = """
Bienvenido al conversor de monedas 🤑
1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos
Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input('¿Cuantos pesos colombianos tienes? : ')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares equivalentes a pesos colombianos") 
elif opcion == 2:
    pass
    pesos = input('¿Cuantos pesos argentinos tienes? : ')
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares equivalentes a pesos argentinos") 
elif opcion == 3:
    pesos = input('¿Cuantos pesos mexicanos tienes? : ')
    pesos = float(pesos)
    valor_dolar = 20
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares equivalentes a pesos mexicanos") 
else:
    print("Ingrese una opción válida")

