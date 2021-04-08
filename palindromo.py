#BUENA PRÁCTICA --> Función principal que corra el programa, se le suele llamar run o main
#Entry point --> Punto de entrada del programa

def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower() #eliminar los espacios y bajar a mayúsculas

    if palabra == palabra[::-1]:
        return True
    else:
        return False

def run(): 
    palabra = input('Escribe una palabra: ')

    if palindromo(palabra) == True:
        print('Es palindromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()