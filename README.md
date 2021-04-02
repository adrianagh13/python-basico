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
- print(5+5)
- 10
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
- nombre = 'Adriana'
- nombre2 = "Gpe"
- nombre + nombre2 
- 'AdrianaGpe'

También podemos multiplicar variables
- nombre * 4
- 'AdrianaAdrianaAdrianaAdriana'

### Boolean
Valores True o False
- es_estudiante = True
- print(es_estudiante)I
- True



## Convertir un tipo de dato a otro
var = input('Ingrese un dato: ') --> Permite la entrada de datos
Si en la entrada de datos no especificamos el tipo de dato, lo identificará como un  string.
- numero1 = input('Escribe un numero' )
- Escribe un numero: 1
- numero1
- "4"

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

