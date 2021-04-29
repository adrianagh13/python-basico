def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    #print(f'{fact}')
    return fact

def es_primo(n):
    m1 = factorial(n-1) % n
    m2 = -1 % n
    #print(f'{m1}  {m2}')
    if factorial(n-1) % n == -1 % n:
        return True
    else:
        return False

def run():
    n = int(input('Ingrese un numero para verificar si es primo o no '))
    if es_primo(n): 
        print('Es primo')
    else:
        print('No es primo')

if __name__ == "__main__":
    run()