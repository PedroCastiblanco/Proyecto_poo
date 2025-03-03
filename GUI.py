#NEW TESTING

import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
from PSO import Enjambre, funcion_objetivo, graf

# Configuración inicial
ctk.set_appearance_mode("dark")


class PSOApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("Algoritmo de optimización por Enjambre de Partículas")

        self.selected_function = ""
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.setup_ui()

    def close(self):
        graf.valid()
        self.destroy()


    def setup_ui(self):
        self.defaults = [0, 0, 0, 0, 0, 0, 0, 0]
        self.label1 = ctk.CTkLabel(self,
                                        text="Bienvenido, con este programa podras calcular los valores máximos y minimos para cualquiera de las siguientes funciones",
                                        fg_color="transparent")

        self.label1.pack(pady=5) # Padding en y

        ctk.CTkLabel(self, text="Selecciona la función de optimización:").pack()

        # self.function_var = ctk.StringVar(value="Sphere")
        self.function_selector = ctk.CTkComboBox(self, values=["Sphere", "Rastrigin", "Rosenbrock","Griewank","Styblinski Tang"],
                                                 command=self.update_function, variable=self.selected_function)
        self.function_selector.pack()


        self.Sphere= ctk.CTkImage(light_image=Image.open('Sphere.png') , size=(200,100))
        self.Rastrigin= ctk.CTkImage(light_image=Image.open('Rastrigin.png'),size=(350,100))
        self.Rosenbrock= ctk.CTkImage(light_image=Image.open('Rosenbrock.png'),size=(350,100))
        self.Griewank= ctk.CTkImage(light_image=Image.open('Griewank.png'),size=(400,100))
        self.Styblinski= ctk.CTkImage(light_image=Image.open('styblinski.png'),size=(350,100))

        self.label_imagen=ctk.CTkLabel(self,text="")
        self.label_imagen.pack( pady=5,padx=200)

        # Recomendaciones
        ctk.CTkLabel(self, text="A continuación, se cargan por defecto los valores sugeridos para obtener el mejor resultado en los cálculos. Sin embargo, recuerda que si quieres puedes cambiarlos a tu gusto",
                                        fg_color="transparent").pack()
        #ctk.CTkLabel(self,
                     #text="Sin embargo, recuerda que si quieres puedes cambiarlos a tu gusto",
                     #fg_color="transparent").pack()

        self.param_frame = ctk.CTkFrame(self)
        self.param_frame.pack()

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

        self.result_label = ctk.CTkLabel(self, text="Resultados")
        self.result_label.pack(pady=10)

    def update_function(self, choice):
        """Actualiza la función seleccionada."""
        self.selected_function = choice
        if (choice == 'Sphere'):
            self.label_imagen.configure(image=self.Sphere)
        elif(choice == 'Rastrigin'):
            self.label_imagen.configure(image=self.Rastrigin)
        elif (choice == 'Rosenbrock'):
            self.label_imagen.configure(image=self.Rosenbrock)
        elif (choice == 'Griewank'):
            self.label_imagen.configure(image=self.Griewank)
        elif (choice == 'Styblinski Tang'):
            self.label_imagen.configure(image=self.Styblinski)
        print('La función elegida fue', self.selected_function)

        # Nuevos valores según la función elegida
        defaults = {
            "Sphere": [50, 500, 0.8, 1.5, 2.0, -1000, 1000, 2],
            "Rastrigin": [50, 2000, 0.8, 1.5, 2.0, -5.12, 5.12, 2],
            "Rosenbrock": [50, 2000, 0.8, 1.5, 2.0, -1000, 1000, 2],
            "Griewank": [50, 2000, 0.8, 1.5, 2.0, -1000, 1000, 2],
            "Styblinski Tang": [50, 2000, 0.8, 1.5, 2.0, -5, 5, 2]
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
        #funcion = lambda x: funcion_objetivo(x, self.selected_function)

        enjambre = Enjambre(num_particulas, funcion_objetivo, x_min, x_max, factor_inercia, factor_personal,
                            factor_social,self.selected_function, dimensiones)
        mejor_posicion, best_value = enjambre.run(iteraciones)

        if(self.selected_function=="Styblinski Tang"):
            self.result_label.configure(text=f"Mejor Posición: {mejor_posicion}\nValor Óptimo: -39.16617 n < {best_value/dimensiones} n < -39.16616 n")
        else:
            self.result_label.configure(text=f"Mejor Posición: {mejor_posicion}\nValor Óptimo: {best_value}")

    def graficar(self):
        graf.graficar(float(self.entries["X Max"].get()))


if __name__ == "__main__":
    app = PSOApp()
    app.mainloop()

