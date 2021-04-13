Tabla de Contenidos - Índice.
___
- [***Características.***](#características)
- [***Estructura de un programa.***](#estructura-de-un-programa)
- [***Literales Variables y Expresiones.***](#literales-variables-y-expresiones)
- [***Operadores y su procedencia.***](#operadores-y-su-procedencia)
- [***Tipos de datos.***](#tipos-de-datos)
  - [Numéricos.](#numéricos)
    - [Enteros (int):](#enteros-int)
    - [Reales (float):](#reales-float)
    - [Conversion tipos de datos.](#conversion-tipos-de-datos)
  - [Booleanos (bool).](#booleanos-bool)
  - [Secuencia - (En Construccion).](#secuencia---en-construccion)
  - [Cadenas de caracteres (En Construccion).](#cadenas-de-caracteres-en-construccion)
    - [Operaciones basicas con cadenas de caracteres.](#operaciones-basicas-con-cadenas-de-caracteres)
      - [Concatenacion.](#concatenacion)
      - [Repeticion.](#repeticion)
      - [Indexacion.](#indexacion)
      - [Longitud.](#longitud)
      - [Comparación.](#comparación)
  - [Tipo de datos mapas o diccionario (dict) (En Construccion).](#tipo-de-datos-mapas-o-diccionario-dict-en-construccion)
- [***Funciones.***](#funciones)
  - [abs(x)](#absx)
  - [divmod(x,y)](#divmodxy)
  - [hex(x)](#hexx)
  - [bin(x)](#binx)
  - [pow(x,y)](#powxy)
  - [round(x,[y])](#roundxy)
  - [input()](#input)
  - [print()](#print)
- [***Creando entornos virtuales.***](#Creando-entornos-virtuales)
- [***Instalando dependencias en entornos virtuales.***](#Instalando-dependencias-en-entornos-virtuales)

- [Ejercicios.](#ejercicios)
- [Creditos.](#creditos)
___

## ***Características.***
  + Es un lenguaje de programación interpretado.
  + De alto nivel.
  + Multi paradigma soportando orientación programada a objetos, imperativa y funcional.
  + Es libre
  + Multiplataforma.
___
## ***Estructura de un programa.***
  - No es necesario reservar ninguna palabra ni función.
  - No es necesario terminar las instrucciones con punto y coma (;) al final de cada linea.
  - Es un lenguaje de programación que respcta la tabulación.
  - La identación se puede hacer con la tecla de espaciado o tab.
  - No es necesario la declaración de variables.
  - El caracter (#) es usado como un comodin para hacer comentarios en el codigo, este no hace parte del código.
___
## ***Literales Variables y Expresiones.***
  - Literales: <p>Los literales son notaciones que permiten representar valores fijos con el codigo de python que cuenta con varios literales como ejemplo estan los Numericos (123) o las cadenas ("soy un literal"). <a href=https://stackoverrun.com/es/q/9423556>Fuente</a> </p>.
    - Enteros: Se representan con cifras enteras ejemplo `(3)(12)(-23)`
    - Reales: Se representan con un punto para separar la parte entera de la decimal. ejemplo `(3.1)(12.10)`.
    - Cadenas: Se representan con con el caracter `'` o doble `""`.
  
  - Variables: Una variable es un identificador que hace referencia a un valor, para que tome este valor se implementa el operador `=` y puede cambiar su valor en cualquier momento.
      ```py
        >>> var = 5
        >>> type(var)
        <class 'int'>
        >>> var = "hola"
        >>> type(var)
        <class 'str'>
    ```
  
  - Expresiones: Es una combinación de variables, literales, operadores, funciones que retornan un valor determinado acorde con la programación generada. 
___  
## ***Operadores y su procedencia.***
  - Los operadores se clasifican segun el tipo de datos con los que se programen, estos son unos ejemplos.
    - Operadores aritméticos: `+, -, *, /, //, %, **`.
    - Operadores de cadenas: `+, *`.
    - Operadores de asignación: `=`.
    - Operadores de comparación:
      - `==`: Igual que.
      - `!=`: Distinto que.
      - `>`: Mayor que.
      - `<`: Menor que.
      - `<=`: Menor o igual.
      - `>=`: Mayor o igual.
    - Operadores lógicos: `and, or, not`.
    - Operadores de pertenencia: `in, not in`.
  - La procedencia de los operadores es la siguiente:
    - Los paréntesis rompen la precedencia.
    - Potencia `(**)`.
    - Unarios `(+ -)`.
    - Multiplicar, dividir, módulo y división entera `(* % // )`.
    - Suma y resta `(+ -)`.
    - Binario `AND (&)` OR y XOR `(^ |)`.
    - Comparación `(<= < > >=)`.
    - Igualdad `(<> == !=)`.
    - Asignación `(=)`.
    - Pertenencia `(in, in not)`.
    - Lógicos `(not, or, and)`.
___  
## ***Tipos de datos.***
Estos son unos de los muchos tipos de datos que existen en python.
### Numéricos.
#### Enteros (int): 
Son todos los enteros (Positivos, Negativos y 0) sin incluir parte decimal.
  - Ejemplo: 
      ```py
        >>> entero = 7
        >>> type(entero)
      ```
#### Reales (float): 
Tienen una parte entera y otra decimal, normalmente se usan de tipo double.
  - Ejemplo: 
      ```py 
        >>> real = 7.2
        >>> type (real)
     ```
#### Conversion tipos de datos.
  - `int(x)`: Convierte el valor a entero.
  - `float(x)`: Convierte el valor a float.
     ```py
        >>> a=int(7.2)
        >>> a
        7
        >>> type(a)
        >>> a=int("345")
        >>> a
        345
        >>> type(a)
        >>> b=float(1)
        >>> b
        1.0
        >>> type(b)
        >>> b=float("1.234")
        >>> b
        1.234
     ```
### Booleanos (bool).
Es parte de la familia de los enteros y se representa con 2 valores Verdadero `True` o Falso `False`.
  - Valores que se interpretan como falso.
    - False.
    - Cualquier numero 0 `(0,0.0)`.
    - Cualquier secuencia vacia `([], (), ‘’)`.
    - Cualquier diccionario vacío `({})`.
### Secuencia - (En Construccion).
  - Tipo lista (list).
  - Tipo tuplas (tuple).
### Cadenas de caracteres (En Construccion).
Las cadenas de caracteres son secuencias que pueden ser almacenadas en variables estas se pueden definir de multiples formas, las mas usuales son con comillas dobles `cad1 = "Hola"`, comillas sencillas `cad2 = 'Hola'` y en bloque con la triple comilla `cad3 = '''Hola, Buen dia'''`.
#### Operaciones basicas con cadenas de caracteres.
##### Concatenacion.
Con el operador ` + ` se pueden unir cadenas de caracteres.
  ```py
    >>> "hola " + "hoy es lunes"
    'hola hoy es lunes'
  ```
##### Repeticion.
Con el operador ` * ` se pueden repetir un dato.
  ```py
      >>> "hola " * 3 
      'holaholahola'
  ```
##### Indexacion.
Se puede obtener el dato de una secuencia indicando la posicion entre los ` [] `.
  ```py
      >>> cadena = "oscar" 
      >>> cadena[1]
      's'
  ```
##### Longitud.
Se puede obtener la longitud de la cadena con la funcion `len()`.
  ```py
      >>> len(cadena)
      5
  ``` 
##### Comparación.
Se puede comparar caracter a caracterobtener la longitud de la cadena con la funcion `len()`.
  ```py
      >>> len(cadena)
      5
  ``` 
### Tipo de datos mapas o diccionario (dict) (En Construccion).
___
## ***Funciones.***
  ### abs(x)
  - Devuelve al valor absoluto de un número.
      ```py
        >>> abs(-2)
        2
      ``` 
  ### divmod(x,y)
  - Toma como parámetro dos números, y devuelve una tubla con dos valores, la división entera, y el módulo o resto de la división.
      ```py
        >>> divmod(9,2)
        (4, 1)
      ```
  ### hex(x)
  - Devuelve una cadena con la representación hexadecimal del número que recibe como parámetro.
      ```py
      >>> hex(250)
      (0xfa)
      ```
  ### bin(x)
  - Devuelve una cadena con la representación binaria del número que recibe como parámetro.
      ```py
      >>> bin(16)
      (0b10000)
      ```
  ### pow(x,y)
  - Devuelve la potencia de la base x elevado al exponente y. Es similar al operador**`.
      ```py
      >>> pow(2,2)
      (4)
      ```
  ### round(x,[y])
  - Devuelve un número real (float) que es el redondeo del número recibido como parámetro, podemos indicar un parámetro opcional que indica el número de decimales en el redondeo.
      ```py
        >>> round(2.546,1)
        (2.5)
      ```
  ### input()
  - Permite obtener por teclado la infofrmacion que se ingresa.
      ```py
        >>> nombre = input("Ingrese su nombre: ") 
        Ingrese su nombre: oscar
        >>> nombre
        'oscar'
      ```
  ### print()
  - Función que permite imprimir por pantalla el dato que se asigna como argumento en los parentesis (argumento).
      ```py
        >>> print(nombre)
        oscar
      ```
  - Con la funcion print tambien se puede dar formato a los datos que se imprimen por pantalla.
    ```py
      >>> print("%d %f %s" % (2.5,2.5,2.5))
      2 2.500000 2.5
    ```
___
## ***Creando entornos virtuales***
- Crear una carpeta del proyecto.
- Comando para crear el entorno virtual.
    ```py
      python3 -m virtualenv venv
    ```
  - Para activar el entorno virtual en linux.
  ```py
      source venv/bin/activate
    ```
  - Para Windows
    ```py
      .\venv\Scripts\activate
    ```
- Comando para des activar el entorno virtual.
  ```py
      deactivate
    ```
- Comando para crear un alias que reduce el comando para el ingreso.
  ```py
      alias avenv=.\venv\Scripts\activate
    ```
- Configurar un alias permanente en linux
  ```py
      - Ejecutar sudo nano ~/.bashrc
      - Ir al final del archivo
      - Agregar el comando: alias avenv='source venv/bin/activate'
      - Guardar el archivo ctrl + o y luego salir con ctrl + x
      - Reejecutar la configuración de la terminal: source ~/.bashrc
      - Activar el entorno vitual avenv
    ```
## ***Instalando dependencias en entornos virtuales***
- Comando para revisar dependencias instaladas
  ```py
      pip3 freeze
    ```
- Comando para instalar dependencias
  ```py
      pip install <paquete>
    ```
- Comando para registrar las dependencias y sus versiones a un archivo plano.
  ```py
      pip3 freeze > requeriements.txt
    ```
- Comando para instalar dependencias registradas en otro entorno virtual.
  ```py
      pip install -r requeriements.txt
    ```
- Comando para desinstalar dependencias
  ```py
      pip uninstall <paquete>
    ```
- Comando 
```py
      pip 
    ```
# Ejercicios.
- Todos los ejemplos se encuentran en la carpeta `examples`.

---
Author
  - Oscar Giovanni Bocanegra
  - https://www.linkedin.com/in/oscarbocanegra/

___
Fuentes.
  - Cursos de [OpenWebinars](https://openwebinars.net/).
  - Cursos de Platzi [Platzi](http://platzi.com/)
___