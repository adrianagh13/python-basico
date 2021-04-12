#contador = 0
#print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)

def run():
    LIMITE = 1000 #en python  las constantes se definen con mayusculas
    contador = 0
    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2)) #recuerda convertir los enteros a str
        contador = contador + 1
        potencia_2 = 2**contador #definimos potencia de nuevo

if __name__ == '__main__':
    run()