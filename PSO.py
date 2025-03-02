import random
import math
import matplotlib.pyplot as plt


# Clase que representa una Partícula
class particula:
    def __init__(self, posicion, velocidad, funcion):
        self.__posicion = posicion  # Posición actual
        self.__velocidad = velocidad  # Velocidad actual
        self.__mejor_posicion = posicion    # Mejor posición personal
        self.__fitness = float('inf')  # Valor de la función objetivo
        self.__funcion = funcion  # Función objetivo

    def set_posicion(self,posicion):
        self.__posicion= posicion
    def get_posicion(self):
        return self.__posicion
    
    def set_velocidad(self,velocidad):
        self.__velocidad= velocidad
    def get_velocidad(self):
        return self.__velocidad
    
    def set_mejor_posicion(self,mejor_posicion):
        self.__mejor_posicion= mejor_posicion
    def get_mejor_posicion(self):
        return self.__mejor_posicion
    
    def set_fitness(self,fitness):
        self.__fitness= fitness
    def get_fitness(self):
        return self.__fitness
    
    def set_funcion(self,funcion):
        self.__funcion= funcion
    def get_funcion(self):
        return self.__funcion

    """Función para evaluar la 'función objetivo' en la posición actual."""
    def evaluar_funcion_objetivo(self):
        self.__fitness = self.__funcion(self.__posicion)
        if self.__fitness < self.__funcion(self.__mejor_posicion):  # Actualiza mejor_posicion si es mejor
            self.__mejor_posicion = self.__posicion[:]

    """Función para actualizar la velocidad y la posición de la partícula."""
    def moverse(self, mejor_posicion_general, factor_inercia, factor_personal, factor_social):
        r1 = random.random()
        r2 = random.random()

        # Actualizar velocidad (elemento por elemento)
        self.__velocidad = [ # Fórmula para actualizar la velocidad
            factor_inercia * v +
            factor_personal * r1 * (p - x) +
            factor_social * r2 * (g - x)
            for v, p, g, x in zip(self.__velocidad, self.__mejor_posicion, mejor_posicion_general, self.__posicion)
        ]
        # Actualizar posición (elemento por elemento)
        self.__posicion = [x + v for x, v in zip(self.__posicion, self.__velocidad)]
        



# Clase que representa el Enjambre
class Enjambre:
    def __init__(self, num_particulas, funcion, x_min, x_max, factor_inercia, factor_personal, factor_social,dimensiones=2):
        self.__particulas = []    # Lista de partículas
        self.__mejor_posicion_global = None  # Mejor posición global
        self.__funcion = funcion  # Función objetivo
        self.__factor_inercia = factor_inercia    # Factor de inercia de las partículas
        self.__factor_personal = factor_personal  # Factor de aprendizaje personal/individual de las partículas
        self.__factor_social = factor_social  # Factor de aprendizaje social/grupal de las partículas
        self.__x_min = x_min  # Límite inferior del espacio de búsqueda
        self.__x_max = x_max  # Límite superior del espacio de búsqueda
        self.__dimensiones = dimensiones     # Dimensiones que se manejarán para el algoritmo


        D=[]
        # Inicializar partículas
        for _ in range(num_particulas):

            # Posiciones para funcion rastring
            posicion = [random.uniform(self.__x_min,self.__x_max) for _ in range(self.__dimensiones)]
            velocidad = [random.uniform(-1, 1) for _ in range(self.__dimensiones)]


            particulax = particula(posicion, velocidad, self.__funcion) 
            D.append(particulax.get_posicion())
            self.__particulas.append(particulax)
        graf.set_posiciones_l(D)
        self.__mejor_posicion_global = self.__particulas[0].get_posicion()[:]


    """Evaluar todas las partículas y actualizar la mejor_posicion_general."""
    def evaluar_enjambre(self):
        for particula in self.__particulas:
            particula.evaluar_funcion_objetivo()
            if self.__funcion(particula.get_mejor_posicion()) < self.__funcion(self.__mejor_posicion_global):
                self.__mejor_posicion_global = particula.get_mejor_posicion()[:]


    """Actualizar la velocidad y la posición de todas las partículas."""
    def actualizar_enjambre(self):
        A=[]
        for particula in self.__particulas:
            particula.moverse(self.__mejor_posicion_global, self.__factor_inercia, self.__factor_personal, self.__factor_social)
            A.append(particula.get_posicion())    
        graf.set_posiciones_l(p_ultimo=A)
        #graf.graficar()

    """Ejecutar el PSO durante un número de iteraciones."""
    def run(self, iteraciones_maximas):
        
        for iteration in range(iteraciones_maximas):
            self.evaluar_enjambre()  # Evalúa partículas
            self.actualizar_enjambre()    # Actualiza partículas


        return self.__mejor_posicion_global, self.__funcion(self.__mejor_posicion_global)

class di2:
    def __init__(self):
        self.__eje_x:list=[]
        self.__eje_y:list=[]
    
    def set_iteracion(self,iteracion):
        self.__iteracion_actual=iteracion

    def get_eje_x(self):
        return self.__eje_x[-1]
    def get_eje_y(self):
        return self.__eje_y[-1]

    def set_posiciones_l(self,p_ultimo:list):
        x,y=[],[]
        for i in p_ultimo:
            x.append(i[0])
            y.append(i[1])
        self.__eje_x.append(x)
        self.__eje_y.append(y)    
    
    def graficar(self):
        
        plt.xlabel("x")
        plt.ylabel("y")

        for i in range(len(self.__eje_x)):
            plt.clf()
            #plt.xlim(min(self.__eje_x[i]),max(self.__eje_x[i]))
            #plt.xlim(min(self.__eje_y[i]),max(self.__eje_y[i]))
            #plt.xlim(-15,15)
            #plt.ylim(-15,15)
            plt.scatter(self.__eje_x[i],self.__eje_y[i],c="red")
            plt.title(f"Posiciones ciclo: {i+1}")
            plt.pause(0.001)
        plt.show()    

        


# Ejemplo para minimizar una función
def funcion_objetivo(x):
    """Ejemplo Sphere funcion """
    #return sum([xi ** 2 for xi in x])  # Suma de los cuadrados de las dimensiones

    """Ejemplo para la función rastrigin"""
    A = 10
    n = len(x)
    #return A * n + sum([xi ** 2 - A * math.cos(2 * math.pi * xi) for xi in x])

    " Ejemplo Rosenbrock function"
    n = len(x)
    return  sum([100*(x[i+1]-(x[i]**2))**2 + (1-x[i])**2   for i in range (n-1)])


"""Parámetros del algoritmo"""
num_particulas = 50      # Número de partículas
factor_inercia = 0.8
factor_personal = 1.5               # Factor cognitivo / personal
factor_social = 2.0                # Factor social / general
iteraciones_maximas = 3 # Número máximo de iteraciones
x_min = -5.15 # Límite inferior
x_max = 5.15 # Límite superior
dimensiones =2 #Dimensiones de la funcion poner entre 2 y 30 

graf=di2()
# Inicializar el enjambre y ejecutar el algoritmo
Enjambre = Enjambre(num_particulas, funcion_objetivo, x_min, x_max, factor_inercia, factor_personal, factor_social,dimensiones)
mejor_posicion, best_value = Enjambre.run(iteraciones_maximas)

# Mostrar el resultado final
print("\nResultados finales:")
print(f"Mejor posición encontrada: {mejor_posicion}")
print(f"Valor óptimo: {best_value}")
graf.graficar()

