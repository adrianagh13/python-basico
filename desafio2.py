while True:
    menu = int(input("""Bienvenido al Restaurante de Nana, ¿qué comerás hoy? :)
        1. Albóndigas
        2. Pozole
        3. Pizza
    """))

    if menu == 1:
        print("Delicioso! Escogiste albóndigas")
        break
    elif menu == 2:
        print("Mmmm, escogiste un rico pozole 😋")
        break
    elif menu == 3:
        print("Mamma mía! Escogiste pizza")
        break
    else:
        print("Ingresaste una opción incorrecta, vuelve a intentar")
        continue

