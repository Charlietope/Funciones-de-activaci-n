# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función tangente hiperbólica y su derivada
def plot_tanh():
    """
    Función que calcula y grafica la función tangente hiperbólica y su derivada.
    """

    # Definición de la función tangente hiperbólica
    def tanh_func(x):
        return np.tanh(x)  # Devuelve la tangente hiperbólica de x
    
    # Derivada de la tangente hiperbólica
    def tanh_deriv(x):
        return 1 - np.tanh(x)**2  # Fórmula de la derivada de tanh(x): 1 - tanh²(x)
    
    # Definir el rango de valores para x
    x = np.linspace(-5, 5, 400)  # Crea un array con 400 valores equidistantes en el rango [-5, 5]
    
    # Evaluar la función tangente hiperbólica en los valores de x
    y = tanh_func(x)
    
    # Evaluar la derivada de la función tangente hiperbólica en los valores de x
    y_deriv = tanh_deriv(x)

    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función tangente hiperbólica
    plt.plot(x, y, label='Tangente Hiperbólica (tanh x)')  
    
    # Graficar la derivada de la función tangente hiperbólica con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función Tangente Hiperbólica y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_tanh()  # Llama a la función para graficar la función tangente hiperbólica y su derivada