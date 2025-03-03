# Proyecto_poo
## Algoritmo PSO(*Particle Swarn Optimization*)
### Explicacion:
La optimización por enjambre de partículas consiste en que cada partícula es una solución potencial al problema de optimización en cuestión; la posición de cada partícula se ajusta de acuerdo a su experiencia y a sus vecinos.

Este método está inspirado en la naturaleza, por ejemplo, el comportamiento que tienen las bandadas de pájaros o bancos de peces en los que,  el movimiento de cada individuo es el resultado de combinar las decisiones individuales de cada una con el comportamiento del resto. 

En pocas palabras los valores de las partículas se actualizan de acuerdo a la mejor posición encontrada en el enjambre, denotada por  “g”.

<p align="center">
  <img src="https://github.com/PedroCastiblanco/Proyecto_poo/blob/main/IMG-20250127-WA0004.jpg" />
</p>


Para actualizar la velocidad de las partículas en el momento “t+1” se calcula de la siguiente manera: 

<p align="center">
  <img src="https://github.com/user-attachments/assets/0d681aee-105c-4600-a896-02c730cd1393" />
</p>

En donde :
 + $\ V_{j}^{(t+1)} \$: La nueva velocidad.
 + $\ V_{j}^{(t)} \$: La velocidad actual.
 + $\ w\$: Reduce o aumenta la velocidad de la partícula.
 + $\ P_1  P_2\$:Son valores aleatoreos en el rango $\ [0,1]\$.
 + $\ I_{j}^{(i)}\$:Mejor posición en la que ha estado la partícula  $\ i\$.
 + $\ X_{j}^{(i)}\$:Posición de la partícula $\ i\$ en el momento $\ t\$.
 + $\ c_1  c_2\$:Constantes de aceleración positivas usadas para escalar la contribución de los componentes cognitivos y sociales.
 + $\ g_j\$:Posición del enjambre en el momento $\ t\$ el mejor valor global.

De esta manera, se crea el siguiente diagrama de clases:
```mermaid
classDiagram
    class Particula {
        -__posicion : list
        -__velocidad : list
        -__mejor_posicion : list
        -__fitness : float
        -__funcion : function
        -__nombre_funcion:str
        +__init__(posicion: list, velocidad: list, funcion: function,nombre_funcion:str)
        +set_posicion(posicion:list)
        +get_posicion():list
        +set_velocidad(velocidad:list)
        +get_velocidad():list
        +set_mejor_posicion(mejor_posicion:list)
        +get_mejor_posicion():list
        +set_fitness(fitness:float)
        +get_fitness():float
        +set_funcion(funcion:any)
        +get_funcion():anu
        +evaluar_funcion_objetivo() 
        +moverse(mejor_posicion_general: list, w: float, c1: float, c2: float) : 
    }

    class Enjambre {
        -__particulas : list
        -__mejor_posicion_global : list
        -__funcion : function
        -__factor_inercia : float
        -__factor_personal : float
        -__factor_social : float
        -__x_min : float
        -__x_max : float
        -__dimensiones : int
        -__funcion_name : str
        +__init__(num_particulas: int, funcion: function, x_min: float, x_max: float, factor_inercia:float, factor_personal:float , factor_social: float,nombre_funcion:str,dimensiones:int=2)
        +evaluar_enjambre()  
        +actualizar_enjambre()  
        +run(iteraciones_maximas: int) :tuple
    }

    class funcion_objetivo {
        +funcion_objetivo(x: list,function_name:str) : float
    }

    class grafica {
        -__eje_x: list 
        -__eje_y: list
        -__estado_w:bool
        +valid()
        +get_eje_x():list
        +get_eje_y():list
        +set_posiciones_l(p_ultimo: list)
        +graficar(xlim:float)
    }
    Enjambre "1"*--"*" Particula
    PSOApp <--Enjambre
    PSOApp <-- grafica

    class PSOApp{
        -selected_function:str
        +__init__()
        +close()
        +setup_ui()
        +update_function(choice:str)
        +run_pso()
        +graficar()
    }
```

A continuación se muestra un diagrama de flujo como resumen del algoritmo:

<p align="center">
  <img src="https://github.com/user-attachments/assets/403c42c0-9d52-4629-a902-e7a80d4b27ce" />
</p>

### Resolución  del problema
Se identificaron 2 conceptos a abstraer los cuales fueron las clases luego denominadas como: **partícula y enjambre**. 

Partícula a  la cual se le dio velocidad, posición y el mejor valor de la misma definido como *fitness*.

En la clase partícula se tienen los métodos evaluar y, mover que evalúan  la función objetivo en la posición actual y actualizan la velocidad y posición de la partícula respectivamente.

Como atributos que varían tenemos los limites  o bordes, la cantidad de iteraciones, la cantidad de partículas y la ecuación que será objetivo , algunos de los cuales se definirán como atributos de la clase enjambre.   

Además de que enjambre distribuye  la cantidad de partículas ingresada uniformemente al inicializarse tiene los métodos **evaluar_enjambre** ,**actualizar_enjambre** y **run**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b2c59f2c-aeb6-4269-864f-77cedb98ff99" />
</p>

Posteriormente  se agregó la interfaz haciendo uso de la librería **Customtkinder** para crear una ventana que contenga *labels* para mostrar las instrucciones, un *comobobox* para elegir entre las 5 ecuaciones disponibles el cual llama un método que cambia la ecuación a usar al seleccionar cualquiera de ellas, además de mostar una imagen de la misma ,junto con un *frame* que tiene los valores default los cuales se pueden variar, valores que al presionar el botón de *Buscar Mínimo* se le enviaran a al método **run** además de la función escogida anteriormente en el *combobox*, también existe un botón *Graficar* que se habilita al usar 2 dimensiones como valor, este llama el método **graficar** de la clase *grafica* que usa la librería **Matplotlib** para graficar la posición de cada punto con su repectivo *x* y *y* en cada iteración y las muestra rápidamente con un *for*.

Aunque estos valores siempre se pueden cambiar es recomendable no poner un límite muy grande ya que para algunas ecuaciones después de cierta dimensión gracias a la aleatoriedad se acercaran a alguno de los otros puntos críticos existentes de la función .Además que al aumentar las dimensiones o el límite es recomendable aumentar las iteraciones.

### Funciones disponibles:
#### Sphere function:
<p align="center">
  <img src="https://github.com/PedroCastiblanco/Proyecto_poo/blob/main/Sphere.png" />
</p>

Que tiene un mínimo global en:

<p align="center">
  <img src="https://github.com/user-attachments/assets/a8babdb5-3e3a-499a-b43a-07173670ef34" />
</p>
Con limites en:
<p align="center">
  <img src="https://github.com/user-attachments/assets/900c5528-91dd-4c5a-a740-73039f6248fa" />
</p>

Pero para mas comodidad se usaran los limites como:  $\ -1000 <= x_i<= 1000 \$

Con una gráfica que muestra los puntos críticos y sus alrededores:
<p align="center">
  <img src="https://github.com/user-attachments/assets/551cde55-5aa2-4f4e-ae96-8278f9715b4f" />
</p>

#### Rastrigin function:
<p align="center">
  <img src="https://github.com/PedroCastiblanco/Proyecto_poo/blob/main/Rastrigin.png" />
</p>

Que tiene un mínimo global en:

<p align="center">
  <img src="https://github.com/user-attachments/assets/a8444516-dbd4-4de4-8092-c9fd51c48aa1" />
</p>
Con limites en:
<p align="center">
  <img src="https://github.com/user-attachments/assets/146f8d8e-580b-40b0-9957-5613e56b6bd9" />
</p>
Con una gráfica que muestra los puntos críticos y sus alrededores:
<p align="center">
  <img src="https://github.com/user-attachments/assets/c0000e0f-735e-413b-a9d1-e7273b99d0ac" />
</p>

#### Rosenbrock function:
<p align="center">
  <img src="https://github.com/PedroCastiblanco/Proyecto_poo/blob/main/Rosenbrock.png" />
</p>

Que tiene un mínimo global en:


<p align="center">
  <img src="https://github.com/user-attachments/assets/b6ff24ad-e8bd-4aef-9509-272e78d9feae" />
</p>
Con limites en:
<p align="center">
  <img src="https://github.com/user-attachments/assets/c6bbd6ec-b8e9-4aa6-9d98-448c1d4189cd" />
</p>


Pero para mas comodidad se usaran los limites como:  $\ -1000 <= x_i<= 1000 \$

Con una gráfica que muestra los puntos críticos y sus alrededores:
<p align="center">
  <img src="https://github.com/user-attachments/assets/e36885f3-f53c-4ad6-928f-23efa95ac9e4" />
</p>



#### Griewank function:
<p align="center">
  <img src="https://github.com/PedroCastiblanco/Proyecto_poo/blob/main/Griewank.png" />
</p>

Que tiene un mínimo global en:
<p align="center">
  <img src="https://github.com/user-attachments/assets/a8444516-dbd4-4de4-8092-c9fd51c48aa1" />
</p>
Con limites en:
<p align="center">
  <img src="https://github.com/user-attachments/assets/900c5528-91dd-4c5a-a740-73039f6248fa" />
</p>

Pero para mas comodidad se usaran los limites como:  $\ -1000 <= x_i<= 1000 \$

Con una gráfica que muestra los puntos críticos y sus alrededores:
<p align="center">
  <img src="https://github.com/user-attachments/assets/21b01ec8-a53e-42f7-8e6d-90c007562587" />
</p>


#### Styblinski–Tang function:
<p align="center">
  <img src="https://github.com/PedroCastiblanco/Proyecto_poo/blob/main/styblinski.png" />
</p>

Que tiene un mínimo global en:

<p align="center">
  <img src="https://github.com/user-attachments/assets/52d8ac22-da7d-4530-9ce3-7af82c8eb479" />
</p>
Con limites en:
<p align="center">
  <img src="https://github.com/user-attachments/assets/17a8ff91-ae65-44cd-9518-171489cd52bf" />
</p>


Con una gráfica que muestra los puntos críticos y sus alrededores:
<p align="center">
  <img src="https://github.com/user-attachments/assets/7d5b9159-bb2a-462a-a11c-45ba5a5ea18d"/>
</p>




## Bibliografía :
+ Comparación de algoritmos de optimización con deferentes funciones y dimensiones |PSO-y-ED-López Núñez Ramírez Rodríguez.pdf
+ [Test functions for optimization](https://en.wikipedia.org/wiki/Test_functions_for_optimization) 
  

## Requisitos para utilizar el programa de manera local
 + Librería customtkinter v 5.2.2 (para la interfaz de usuario)
