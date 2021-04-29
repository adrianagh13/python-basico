def es_primo(numero):
contador = 0 #llevará la cuenta de los numeros entre los que se va dividieno el numero ingresado

for i in range(1, numero + 1):
    if i == 1 or i == numero:
        continue #la sentencia continue se saltea la vuelta del ciclo
    if numero % i == 0:
        contador += 1 
        break #Si un numero es divisible entre cualquier otro numero, eso indicaría que no es primo por lo tanto ponemos un break para que no se siga iterando innecesariamente
if contador == 0:
    return True
else:
    return False


def run():
    numero = int(input("Ingrese un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()