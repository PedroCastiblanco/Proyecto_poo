```mermaid
classDiagram
    class Particula {
        -posicion : list
        -velocidad : list
        -mejor_posicion : list
        -fitness : float
        -funcion : function
        +__init__(posicion: list, velocidad: list, funcion: function)
        +evaluar_funcion_objetivo() : void
        +moverse(mejor_posicion_general: list, w: float, c1: float, c2: float) : void
    }

    class Enjambre {
        -particulas : list
        -mejor_posicion_global : list
        -funcion : function
        -factor_inercia : float
        -factor_personal : float
        -factor_social : float
        -x_min : float
        -x_max : float
        +__init__(num_particulas: int, funcion: function, x_min: float, x_max: float, w: float, c1: float, c2: float)
        +evaluar_enjambre() : void
        +actualizar_enjambre() : void
        +run(iteraciones_maximas: int) : tuple
    }

    class funcion_objetivo {
        +funcion_objetivo(x: list) : float
    }

    Enjambre "1"*--"*" Particula
```
