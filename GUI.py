#NEW TESTING

import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import math
from PSO import Enjambre, funcion_objetivo, graf

# Configuración inicial
ctk.set_appearance_mode("dark")


class PSOApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x700")
        self.title("Algoritmo de optimización por Enjambre de Partículas")

        self.selected_function = ""
        self.setup_ui()

    def setup_ui(self):
        self.defaults = [0, 0, 0, 0, 0, 0, 0, 0]
        self.label1 = ctk.CTkLabel(self,
                                        text="Bienvenido, con este programa podras calcular los valores máximos y minimos para cualquiera de las siguientes funciones",
                                        fg_color="transparent").pack(pady=20)

        ctk.CTkLabel(self, text="Selecciona la función de optimización:").pack(pady=10)

        # self.function_var = ctk.StringVar(value="Sphere")
        self.function_selector = ctk.CTkComboBox(self, values=["Sphere", "Rastrigin", "Rosenbrock"],
                                                 command=self.update_function, variable=self.selected_function)
        self.function_selector.pack(pady=10)


        # Recomendaciones
        ctk.CTkLabel(self, text="A continuación, se cargan por defecto los valores sugeridos para obtener el mejor resultado en los cálculos.",
                                        fg_color="transparent").pack()
        ctk.CTkLabel(self,
                     text="Sin embargo, recuerda que si quieres puedes cambiarlos a tu gusto",
                     fg_color="transparent").pack()

        self.param_frame = ctk.CTkFrame(self)
        self.param_frame.pack(pady=10)

        self.entries = {}
        params = ["Num Partículas", "Iteraciones", "Factor Inercia", "Factor Personal", "Factor Social", "X Min",
                  "X Max", "Dimensiones"]


        for i, (param, default) in enumerate(zip(params, self.defaults)):
            label = ctk.CTkLabel(self.param_frame, text=param)
            label.grid(row=i, column=0, padx=10, pady=5)
            entry = ctk.CTkEntry(self.param_frame)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, str(default))
            self.entries[param] = entry

        self.min_button = ctk.CTkButton(self, text="Buscar Mínimo", command=self.run_pso)
        self.min_button.pack(pady=10)

        #Botón para graficar:
        self.graficar_button = ctk.CTkButton(self, text="Graficar", command=self.graficar, state="disabled")
        self.graficar_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="Resultados:")
        self.result_label.pack(pady=10)

    def update_function(self, choice):
        """Actualiza la función seleccionada."""
        self.selected_function = choice
        print('La función elegida fue', self.selected_function);

        # Nuevos valores según la función elegida
        defaults = {
            "Sphere": [50, 500, 0.8, 1.5, 2.0, -5.15, 5.15, 2],
            "Rastrigin": [50, 200, 0.8, 1.5, 2.5, -100000, 100000, 2],
            "Rosenbrock": [50, 200, 0.8, 1.5, 2.5, -100000, 100000, 2]
        }

        # Obtener los valores de la función seleccionada
        new_defaults = defaults.get(choice, [0] * 7)  # Evita errores si se selecciona una opción no definida

        # Actualizar los valores en los campos de entrada
        for entry, new_value in zip(self.entries.values(), new_defaults):
            entry.delete(0, "end")  # Borrar valor actual
            entry.insert(0, str(new_value))  # Insertar nuevo valor




    def run_pso(self):
        print('Entra aquí')
        """Ejecuta la optimización por enjambre de partículas y actualiza la interfaz."""
        num_particulas = int(self.entries["Num Partículas"].get())
        iteraciones = int(self.entries["Iteraciones"].get())
        factor_inercia = float(self.entries["Factor Inercia"].get())
        factor_personal = float(self.entries["Factor Personal"].get())
        factor_social = float(self.entries["Factor Social"].get())
        x_min = float(self.entries["X Min"].get())
        x_max = float(self.entries["X Max"].get())
        dimensiones = int(self.entries["Dimensiones"].get())
        if dimensiones == 2:
            self.graficar_button.configure(state="normal")
        else:
            self.graficar_button.configure(state="disabled")

        #Para utilizar la función apropiada en PSO.py
        funcion = lambda x: funcion_objetivo(x, self.selected_function)

        enjambre = Enjambre(num_particulas, funcion, x_min, x_max, factor_inercia, factor_personal,
                            factor_social, dimensiones)
        mejor_posicion, best_value = enjambre.run(iteraciones)

        self.result_label.configure(text=f"Mejor Posición: {mejor_posicion}\nValor Óptimo: {best_value}")

    def graficar(self):
        graf.graficar()


if __name__ == "__main__":
    app = PSOApp()
    app.mainloop()

