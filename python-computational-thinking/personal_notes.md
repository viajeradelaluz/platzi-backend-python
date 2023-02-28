# Introducción al pensamiento computacional con Python

**[platzi](https://platzi.com/clases/python-cs/) | David Aroesti**

<br>

## Introducción al pensamiento computacional

### Introducción al cómputo

#### **Historia del cómputo**

¿Qué significa computar? Contar o calcular algo numéricamente, ya sea el tiempo, la edad, las posiciones de los objetos.

> En matemáticas hay dos tipos de razonamiento: el simbólico y el visual. El razonamiento simbólico tuvo su origen en la notación numeral y se desarrolló con el álgebra. El razonamiento visual se desarrolla en la geometría que después del número, introduce un segundo concepto importante en la disciplina: **la forma**.
>
> Ian Stewart - Historia de las matemáticas.

#### **Algunas máquinas computadoras**

- Relojes de sol antiguos.
- Telar de Jacquard: tarjetas perforadas que representan información.
- Motor analítico de Charles Babbage, generara cálculos mediante engranajes separando las instrucciones del cálculo. Usado por Ada Lovelace, considerada la primera programadora de ordenadores, calculó la serie de números de Bernoulli.
- Máquina de Alan Turing y funciones de Alonzo Church.
- ENIAC (Electronic Numerical Integrator and Computer), primera computadora digital, usaba sistema decimal.
- EDVAC (Electronic Discrete Variable Automatic Computer), usaba sistema binario en arquitectura Von Neumann:
  - Dispositivo de entrada.
  - Unidad central de procesamiento de los cálculos.
  - Dispositivo de salida.
- Grace Hopper, líder del desarrollo de uno de los primeros lenguajes de alto de nivel en implementarse: COBOL.
- Microchips.
- En el siglo XX, el físico Richard Feynman aporta las bases matemáticas para el cómputo cuántico.

<br>

### Introducción a los lenguajes de programación

#### **Dar instrucciones a las máquinas**

Hacemos esto a través de los _paradigmas de programación_. Estos paradigmas se definen por su forma de abordar un problema o las herramientas utilizadas para resolverlo, lo que da lugar a la clasificación de lenguajes y estilos de programación.

#### **Paradigmas de programación**

La clasificación más común incluyen el **paradigma imperativo**, en el que el programador da instrucciones paso a paso para ser ejecutadas por la máquina, se enfoca en el cómo llegar a un resultado y cómo son ejecutados los procesos a través de estructuras de control.

- **Algoritmo**

  > Un algoritmo es una lista finita de instrucciones que describen un cómputo, que cuando se ejecuta con ciertas entradas (inputs) ejecuta pasos intermedios para llegar a un resultado (output).
  > John V. Guttag

|                                      |                                                  Premisa                                                   |                                              Características                                               |         Lenguajes          |
| :----------------------------------: | :--------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :------------------------: |
|    **Programación estructurada**     |                Evitar el uso de "goto" para seguir una serie de instrucciones en secuencia.                | Utilizaba estructuras de control, entradas/salidas, manejo de errores, excepciones y estructuras de datos. | Fortran Pascal COBOL Ada C |
|     **Programación procedural**      |                   El código se agrupa en procedimientos a través de un sistema de pilas.                   |                 El programa se compone de procedimientos los cuales interactúan entre sí.                  | Fortran ALGOL COBOL Basic  |
| **Programación orientada a objetos** | Los objetos de la vida real pueden ser representados en código, con sus características y comportamientos. |    Los objetos son un molde para crear instancias con cualidades y comportamientos únicos o compartidos    | Simula Java C++ Python PHP |

Por otro lado, el **paradigma declarativo** se enfoca en el resultado más allá del cómo, nos dice el tipo de relaciones que existe entre las variables. También procura reducir los efectos colaterales derivados de la ejecución de los programas.

|                            |                                                         Premisa                                                         |                                      Características                                       |               Lenguajes               |
| :------------------------: | :---------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: | :-----------------------------------: |
| **Programación funcional** | Las funciones pueden ser tratadas como variables y en cualquier parte del código, busca reducir los efectos colaterales |      La recursividad y funciones de alto orden son prioridad para resolver problemas       | Lisp Scheme Clojure Erlang Haskell F# |
|  **Programación lógica**   |                     Expresa los objetivos como reglas acerca de los resultados en lógica matemática                     | Hace uso de Cláusulas de Horn para evaluar predicados y definir si son verdaderos o falsos | Prolog ALF Fril Visual-Prolog Mercury |

Finalmente, estos son otros paradigmas o modelos de computación:

|                                       |                                     Premisa                                     |                                                          Características                                                          |         Lenguajes         |
| :-----------------------------------: | :-----------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------: | :-----------------------: |
| **Programación dirigida por eventos** | No controla la secuencia de ejecuciones, sino que reacciona a sucesos ocurridos |                     Son programas que corren indefinidamente, cambian su estado según los eventos que detecta                     | Java JavaScript C# Python |
|     **Programación concurrente**      |    Usa el paralelismo para dividir las tareas entre los recursos disponibles    | Los programas tienen dos o más contextos de ejecución divididos (procesadores o hilos) para manejar las peticiones entre recursos |     Javascript GO C#      |

<br>
<br>

## Introducción a Python

### **Garbage collector (GC)**

Administra de forma automática la memoria, ya que es el encargado de liberar los objetos que ya no están en uso.

## Programas numéricos

- **Enumeración exhaustiva:** también llamado 'adivina y verifica' o 'búsqueda de fuerza bruta'. Se enumeran todas las posibilidades para la solución de un problema. Ver: problema de las ocho reinas.
- **Aproximación de soluciones:** similar a la enumeración exhaustiva, pero no necesita una respuesta exacta. Las soluciones se aproximan con un margen de error llamado épsilon.
- **Búsqueda binaria:** es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración. La respuesta debe encontrarse en un conjunto ordenado.

## Funciones, alcance y abstracción

### **Abstracción**

No es necesario entender la forma en la que algo opera internamente para poderlo utilizar. Se usa para encapsular el código y definir una interfaz pública. Ej. Calculadora.

### **Descomposición**

Permite dividir el código en unidades lógicas que colaboran en un programa mayor.

### **Scope o alcance**

Contextos de ejecución de las variables. Python lee los programas de arriba hacia abajo y de izquierda a derecha.

- **Alcance global:** variables creadas en el cuerpo principal del código.
- **Alcance local:** variables creadas dentro de métodos, estas variables desaparecen después de la ejecución del contexto de ejecución.

### **Especificaciones del código**

Docstring que detalla el modo de usar una función.

### **Recursividad**

- **Algorítmica:** Una forma de crear soluciones utilizando el principio de "divide y vencerás".
- **Programática:** Técnica en la cual una función se llama así misma.

## Tipos estructurados, mutabilidad y funciones de alto nivel

### **Funciones como objetos**

Las funciones en Python son 'ciudadanas de primer orden', pueden ser tratadas como variables/objetos y en cualquier parte del código.

### **Tuplas**

Son secuencias inmutables de objetos, pueden contener cualquier tipo de objeto, se pueden desempaquetar y pueden utilizarse para devolver varios valores en una función.

**Rangos**
Representan una secuencia de enteros. Ej. `range(comienzo, fin, pasos)`, también son inmutables y muy eficientes en uso de memoria. Normalmente utilizados en loops.

**Listas y mutabilidad**
Son secuencias de objetos modificables (mutables). Como se pueden ampliar hay que tener en cuenta los efectos secundarios de ampliar la memoria. Es posible iterar con ellas.

- **Clonación:** Casi siempre es mejor clonar una lista que mutarla, para ello, se puede usar `slices[::]` o `list`.
- **List comprehension:** Es una forma de concisa de aplicar operaciones a los valores de una secuencia, utilizando filtros.

```pycon
>>> a = list(range(100))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> double = [i * 2 for i in a]
>>> double
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
>>> pares = [i for i in a if i % 2 == 0]
>>> pares
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
```

### **Diccionarios**

Son como listas, pero en lugar de usar índices utilizan llaves, también son mutables, no tienen orden interno y pueden iterarse.

## Pruebas y debugging

### **Pruebas de caja negra**

Se basan en la especificación de la función o el programa. Prueba inputs y valida outputs.

- **Unit testing:** Pruebas unitarios del código función por función.
- **Integration testing:** Verificar que todos los modulos que funcionan entre si.

### **Pruebas de caja de cristal**

Se basan en el flujo del programa, es decir, se asume que se conoce la implementación del mismo. Se centra en probar las diferencias o caminos que existen en las funciones (ciclos, recursión, etc). Efectiva para hacer _regression testing_ o _mocks_ para determinar donde se encuentras los bugs que aparecen luego de lanzar un programa.

- **Ejemplo:** en un ciclo `while` se podrían hacer una prueba en donde la condición del ciclo sea falsa y una prueba para analizar el comportamiento de los `break statement`.

También debemos probar todas las exepciones que pueda tener nuestro código, es decir, los errores.

### **Debugging**

Utiliza los datos disponibles para crear hipótesis y experimentos. (Método científico). Lleva un resgistro de lo que has tratado, preferiblemente en forma de tests. La pregunta no es en qué está fallando, sino cómo está computando nuestro programa.

- **Diseño de experimentos:** Debugear es un proceso de búsqueda. Cada prueba debe acotar el espacio de búsqueda. _Búsqueda binaria con print statements_.

## Excepciones y afirmaciones

### **Manejo de excepciones**

Sirven para poder ramificar programas. No deben manejarse de manera silenciosa, por ejemplo con print statement. Cuando una excepción no se manejra, el programa termina en error. Se pueden crear excepciones propias.

### **Excepciones y control de flujo**

Existen dos principios para controlar el control de flujo, el EAFP (Easier to Ask for Forgiveness than Permission) _Es más fácil pedir perdón que permiso_, y el LBYL (Look Before You Leap) _Revisa antes de saltar_.

```python
def busca_pais_eapf(paises, pais):
  """ Principio EAFP """
  try:
    return paises[pais]
  except KeyError:
    return None

def busca_pais_lbyl(paises, pais):
  """ Principio LBYL """
  if not isinstance(paises, dict):
    return None
  return paises[pais]
```

### **Afirmaciones**

Mecanismo para determinar si una condición se cumple o no, y poder seguir adelante con nuestro programa o terminar dicha excepción.

- Método de programación defensiva, es decir, nos preparamos para determinar si los inputs son del tipo que esperamos.
- Pueden utilizarse para verificar que los tipos sean correctos en una función.
- También sirven para debuguear.

```python
# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_palabras):
  primeras_letras = []

  for palabra in lista_palabras:
    assert type(palabra) == str, f"{palabra} no es str"
    assert len(palbra) > 0, "No se permiten str vacíos"

    primeras_letras.append(palabra[0])

  return primeras_letras
```
