import random
import math
import matplotlib.pyplot as plt

# Clase que representa una Partícula
class particula:
    def __init__(self, posicion, velocidad, funcion):
        self.posicion = posicion  # Posición actual
        self.velocidad = velocidad  # Velocidad actual
        self.mejor_posicion = posicion    # Mejor posición personal
        self.fitness = float('inf')  # Valor de la función objetivo
        self.funcion = funcion  # Función objetivo

    """Función para evaluar la 'función objetivo' en la posición actual."""
    def evaluar_funcion_objetivo(self):
        self.fitness = self.funcion(self.posicion)
        if self.fitness < self.funcion(self.mejor_posicion):  # Actualiza mejor_posicion si es mejor
            self.mejor_posicion = self.posicion[:]

    """Función para actualizar la velocidad y la posición de la partícula."""
    def moverse(self, mejor_posicion_general, factor_inercia, factor_personal, factor_social):
        r1 = random.random()
        r2 = random.random()

        # Actualizar velocidad (elemento por elemento)
        self.velocidad = [ # Fórmula para actualizar la velocidad
            factor_inercia * v +
            factor_personal * r1 * (p - x) +
            factor_social * r2 * (g - x)
            for v, p, g, x in zip(self.velocidad, self.mejor_posicion, mejor_posicion_general, self.posicion)
        ]
        # Actualizar posición (elemento por elemento)
        self.posicion = [x + v for x, v in zip(self.posicion, self.velocidad)]

fig = plt.figure()
ax = fig.add_subplot()
fig.show()

A=[]

# Clase que representa el Enjambre
class Enjambre:
    def __init__(self, num_particulas, funcion, x_min, x_max, factor_inercia, factor_personal, factor_social):
        self.particulas = []    # Lista de partículas
        self.mejor_posicion_global = None  # Mejor posición global
        self.funcion = funcion  # Función objetivo
        self.factor_inercia = factor_inercia    # Factor de inercia de las partículas
        self.factor_personal = factor_personal  # Factor de aprendizaje personal/individual de las partículas
        self.factor_social = factor_social  # Factor de aprendizaje social/grupal de las partículas
        self.x_min = x_min  # Límite inferior del espacio de búsqueda
        self.x_max = x_max  # Límite superior del espacio de búsqueda
        dimensiones = 2     # Dimensiones que se manejarán para el algoritmo

        # Inicializar partículas
        for _ in range(num_particulas):

            # Posiciones para funcion rastring
            posicion = [random.uniform(x_min, x_max) for _ in range(dimensiones)]
            velocidad = [random.uniform(-1, 1) for _ in range(dimensiones)]


            particulax = particula(posicion, velocidad, funcion) 
            self.particulas.append(particulax)

        self.mejor_posicion_global = self.particulas[0].posicion[:]


    """Evaluar todas las partículas y actualizar la mejor_posicion_general."""
    def evaluar_enjambre(self):
        for particula in self.particulas:
            particula.evaluar_funcion_objetivo()
            if self.funcion(particula.mejor_posicion) < self.funcion(self.mejor_posicion_global):
                self.mejor_posicion_global = particula.mejor_posicion[:]


    """Actualizar la velocidad y la posición de todas las partículas."""
    def actualizar_enjambre(self):
        for particula in self.particulas:
            particula.moverse(self.mejor_posicion_global, self.factor_inercia, self.factor_personal, self.factor_social)


    """Ejecutar el PSO durante un número de iteraciones."""
    def run(self, iteraciones_maximas):
        for iteration in range(iteraciones_maximas):
            self.evaluar_enjambre()  # Evalúa partículas
            self.actualizar_enjambre()    # Actualiza partículas
            A.append(self.funcion(self.mejor_posicion_global))
            ax.plot(A,color="r")
            fig.canvas.draw()
            ax.set_xlim(left=max(0,iteration-iteraciones_maximas), right=iteration+3)

        return self.mejor_posicion_global, self.funcion(self.mejor_posicion_global)


# Ejemplo para minimizar una función
def funcion_objetivo(x):
    """Ejemplo Sphere funcion """
    return sum([xi ** 2 for xi in x])  # Suma de los cuadrados de las dimensiones

    """Ejemplo para la función rastrigin"""
    A = 10
    n = len(x)
    return A * n + sum([xi ** 2 - A * math.cos(2 * math.pi * xi) for xi in x])


"""Parámetros del algoritmo"""
num_particulas = 50      # Número de partículas
factor_inercia = 0.8
factor_personal = 1.5               # Factor cognitivo / personal
factor_social = 2.0                # Factor social / general
iteraciones_maximas = 500 # Número máximo de iteraciones
x_min = -5.15 # Límite inferior
x_max = 5.15 # Límite superior

# Inicializar el enjambre y ejecutar el algoritmo
Enjambre = Enjambre(num_particulas, funcion_objetivo, x_min, x_max, factor_inercia, factor_personal, factor_social)
mejor_posicion, best_value = Enjambre.run(iteraciones_maximas)

# Mostrar el resultado final
print("\nResultados finales:")
print(f"Mejor posición encontrada: {mejor_posicion}")
print(f"Valor óptimo: {best_value}")
plt.show()
