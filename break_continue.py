def run():
    # for contador in range(1000): #unicamente imprimimos numeros pares
    #     if contador % 2 != 0:
    #         continue #si se cumple la condicion lo que se encuentra debajo de la sentencia continue no se ejecuta
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break #esta sentencia rompe el ciclo si se cumple la condicion

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == "__main__":
    run()