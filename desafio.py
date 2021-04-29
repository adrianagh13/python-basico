import random

def juego():
    opcion = input("Ingresa un numero")
    return opcion

def run():
    ganadas_usuario = 0
    ganadas_sistema = 0
    rondas = 0
    print("""PIEDRA, PAPEL O TIJERA ✂ 
    Instrucciones: Ingresa la opcion por número, tienes 5 rondas para ganar!
    1. Piedra
    2. Papel
    3. Tijera
    """)

    while rondas < 5:
        usuario = juego()
        maquina = random.randrange(3)
        rondas += 1

        if usuario

if __name__ == '__main__':
    run()