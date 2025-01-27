# Proyecto_poo
## Algoritmo PSO(*Particle Swarn Optimization*)
### Explicacion:
La optimización por enjambre de partículas consiste en que cada partícula es una solución potencial al problema de optimización en cuestión; la posición de cada partícula se ajusta de acuerdo a su experiencia y a sus vecinos.

Este método está inspirado en la naturaleza, por ejemplo, el comportamiento que tienen las bandadas de pájaros o bancos de peces en los que,  el movimiento de cada individuo es el resultado de combinar las decisiones individuales de cada una con el comportamiento del resto. 

En pocas palabras los valores de las partículas se actualizan de acuerdo a la mejor posición encontrada en el enjambre, denotada por  “g” .Para actualizar la velocidad de las partículas en el momento “t+1” se calcula de la siguiente manera: 

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



