# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función escalón (Heaviside) y su derivada aproximada
def plot_step_function():
    """
    Función que calcula y grafica la función escalón (Heaviside) y su derivada aproximada.
    """

    # Definición de la función escalón (Heaviside)
    def step_function(x):
        return np.where(x < 0, 0, 1)  # Devuelve 0 si x < 0, y 1 si x >= 0
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)  # Crea un array de 400 valores equidistantes en el rango [-10, 10]
    
    # Evaluar la función escalón en los valores de x
    y = step_function(x)
    
    # Derivada aproximada de la función escalón
    y_deriv = np.zeros_like(x)  # La derivada es 0 en casi todo el dominio (excepto en x=0, que es una discontinuidad)
    
    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función escalón
    plt.plot(x, y, label='Función Escalón')  
    
    # Graficar la derivada aproximada (línea punteada de color verde)
    plt.plot(x, y_deriv, label='Derivada (aproximada)', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función Escalón y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_step_function()  # Llama a la función para graficar la función escalón y su derivada