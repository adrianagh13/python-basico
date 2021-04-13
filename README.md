# Curso Básico de Python
Apuntes del curso básico de Python.

## ¿Por qué aprender python?
- Tiene una estructura elegante y definida, está en contacto con el inglés.
- Ayuda a tener buenas prácticas.
- Se puede implementar en áreas de IOT, Backend, AI y Data Science.
- Instagram, Google, Spotify y demás, están desarrollados en el backend con python.



## Núcleo de un programa: los algoritmos
Se trata de una serie de pasos ordenados que permiten resolver un problema. 
- Todos los algoritmos son finitos, siempre hay una cantidad limitada de pasos.
- No es ambiguo.



## Explorando Python: operadores aritméticos
Para utilizar la consola interactiva de python se ejecuta el comando py o python3. Para identificar que se activó la consola interactiva, debemos ver esto >>>.
Podemos hacer operaciones ariméticas, como sumas, restas. Sin embargo, en el editor de código no es así, debemos imprimir el valor.  
print(5+5)  
10  

- // --> Devuelve la parte entera de una división
- % --> Residuo de una división 
- ** --> Permite realizar potencias
- num**(1/n) --> Raíz, donde n es el orden de la raíz.



## PRIMITIVOS: Tipos de datos sencillos
En python todos los datos son objetos, a diferencia del paradigma de POO.
Podemos encontrar 4 tipos de datos que vienen definidos por defecto en python, son los datos primitivos.

### Integer
Todos los números enteros

### Float
Números de punto flotante. En python se representan con un punto, no con coma. 4.3 != 4,3

### Strings
Es indiferente si utilizamos comillas simples o comillas dobles
Podemos operar con las cadenas de texto. Por ejemplo, para concatenar, sumamos dos variables.    
nombre = 'Adriana'  
nombre2 = "Gpe"  
nombre + nombre2  
'AdrianaGpe'

También podemos multiplicar variables  
nombre * 4  
'AdrianaAdrianaAdrianaAdriana'

### Boolean
Valores True o False  
es_estudiante = True  
print(es_estudiante)  
True



## Convertir un tipo de dato a otro
var = input('Ingrese un dato: ') --> Permite la entrada de datos
Si en la entrada de datos no especificamos el tipo de dato, lo identificará como un  string.  
numero1 = input('Escribe un numero' )  
Escribe un numero: 4  
numero1  
"4"  

### Convertir a entero
- int(numero1) --> Convierte un dato o variable en entero. Esta sentencia nos arrojará el valor en consola, sin embargo podemos guardarlo en un variable.
- numero1 = int(numero1)

También es una buena práctica especificar el tipo de dato entero desde la entrada de datos.
- numero1 = int(input("Ingrese un numero "))

### Convertir a string
- str(numero1) --> Convierte un dato o variable en string. Esta sentencia nos arrojará el valor en consola, sin embargo podemos guardarlo en un variable.



## Operadores lógicos y de comparación

### Lógicos
- es_estudiante = True
- trabaja = False

#### and
- and --> Para que retorne verdadero, todas las variables que se comparen tienen que ser verdaderas.
- es_estudiante and trabaja
- False

#### or
- or --> Para que retorne verdadero si al menos una de las variables comparadas tienen que ser verdaderas.
- es_estudiante or trabaja
- true

#### not
- not --> Invierte el valor lógico del bool
- not trabaja
- True

### Comparación
- == --> Igualdad: devuelve verdadero si 2 valores son iguales
- != --> Diferencia: Devuelve verdadero si los valores son diferentes.
- > --> Mayor que
- < --> Menor que
- >= --> Mayor igual
- <= --> Menor igual



## Conversor
Realizamos un algoritmo que convierte una cantidad de pesos a dolares. Implementamos una nueva función llamada round, la cual redondea un numero flotante al numero de decimales que se le indiquen.
- round(var, n)



## Condicionales
- El condicional **if** (si) permite identificar si una sentencia se cumple o no. Seguido de la sentencia van 2 puntos : que indican que se ejecutará códido respecto al cumplimiento de la sentencia
Sintáxis: if n > 2:
- **elif** (en cambio si)--> Condicional posterior al if, pero no esl final. Lo podemos usar las veces que sean
- **else** (en cambio) --> El último condicional a aplicar

Para las instrucciones de los condicionales debe haber 4 espacios (indentación).

Extra: la sentencia **pass** indica una instrucción que omitiremos por el momento, es código de relleno



## Funciones 

### Definición
- En python una función es un código reutilizable que toma argumentos, realiza algunos cálculos y devuelve uno o más resultados. 
Para definir una función utilizamos la palabra reservada **def**.
- Llamamos o invocamos la función utilizando una expresión que contenga el nombre de la función, paréntesis para posibles parámetros, y argumentos dentro de ellos. Se puede invocar las veces que sea necesario.

### Tipos de funciones

#### Incorporadas
- Son parte de python: **print(), round(), int(), type()...**
[Built-in functions](https://docs.python.org/3/library/functions.html)
#### Definición propia
- Creadas por el programador con **def**, para después utilizarlas, seguida de parámetros opcionales entre paréntesis y 2 puntos. 
- Se indenta el cuerpo de la función
- Define la función pero no la llama.

### Parámetros
Un parámetro es una variable que utilizamos en las funciones. Permite al código de la función acceder a los argumentos recibidos. Los parámetros hacen que los argumentos se reciban por orden.

### Argumentos
- Es un valor que informamos a la función como su input cuando llamamos a la función. Los utilizamos para instruir a la función que realice diferentes tareas. 
- Podemos llamar a la función indicando los argumentos por posición o por nombre de los parámetros. 
- También se pueden definir un número indeterminado de argumentos creando una lista dinámica tipo tupla, definiendo el parámetro con un asterisco.

### Sentencia return 
Las funciones pueden comunicarse con el exterior de las mismas. El proceso de comunicación con el exterior se hace devolviendo valores usando la sentencia **return**. Por defecto todas las funciones retornan el valor none.



## Trabajando con texto: Cadenas de caractéres

Métodos: Función especial para un tipo de dato en particular.  

Para las cadenas de texto podemos implementar diferentes métodos principalmente de las funciones ya integradas. Algunos de ellos que vimos en clase son:
- upper(): Convierte a mayúsculas una cadena.
- capitalize(): Pone mayúscula a la primer letra de una cadena.
- strip(): Elimina espacios al inicio y al final de una cadena.
- lower(): Convierte a minúsculas una cadena.
- replace('a', 'b'): Reemplaza cierta letra en una cadena, donde a es la letra a reemplazar, y b es el reemplazo.
- len(string): Retorna la longitud de una cadena.

**Indices** También, podemos acceder a los caracteres de una cadena mediante indices:  ej --> string[0]

**Slices** Permiten dividir una cadena en "rebanadas", de múltiples formas:  
nombre = 'Adriana'  
nombre[0:3]  
'Adr'

[Tipos de Métodos Built-in: Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)



## Proyecto: Palindromo  

Palíndromo: Palabra con el mismo significado leyéndose al derecho y al revés.  
Aplicamos métodos de cadenas de caracteres, condicionales, operadores de comparación, y además implementamos la función principal run.



## Función principal run y Entry Point
Todos los programas de python tienen una función principal que contiene la lógica del archivo. Esta función se le llama run o main.  
def run()  

Hay código que unicamente queremos usar cuando corremos un archivo, y hay otro que queremos correr siendo importado. Podemos distinguir esta diferencia utilizando la siguiente sentencia:  
if __name__ = "__main__"  
    run()
Al correr un código python se hacen asignaciones de variables. A la variable name se le asigna el string main. Con esta asignación corremos la función principal.  
Este condicional permite que el código del programa original, sea diferente a un programa al que se le importe, pues ya no corre desde el programa original.  

[Sentencia de entry point](https://www.youtube.com/watch?v=sugvnHA7ElY)



## Aprendiendo bucles

### While  
Se trata del ciclo fundamental de la programación.  
While --> Mientras  
Misma estructura que un condicional:  
while ***sentencia***:  
    pass  

Extra: No podemos concatener ints y strings a la vez, debemos de convertir los numeros. Si no deseamos convertir debemos poner una f entre los paréntesis, y las variables entre corchetes:  
print(f'2 elevado a la {contador} es igual a {potencia_2}')

### For  
Este ciclo será usado cuando se conozcan la cantidad de veces a iterar. Se utiliza para recorrer los elementos de un objeto iterable.  
Sintáxis: for contador in range(inicial:tope):  
- Un **contador** es una variable que contiene valores que van incrementando o decrementando cada vez que se ejecuta una acción que lo contenga. También se escribe como **i** por iterador.  
- La función incorporada **range()** retorna una sucesión de numeros enteros, se utiliza para representar una secuencia inmutable de números.  
Podemos recorrer cadenas de caracteres o Strings con for, simplemente iterando la variable de la palabra o frase:  
for caracter in palabra:
    print(caracter)
 







