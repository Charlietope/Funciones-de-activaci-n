import numpy as np  # Biblioteca para operaciones numéricas con arreglos
import matplotlib.pyplot as plt  # Biblioteca para la creación de gráficos

from src.relu import plot_relu  # Función para graficar la función ReLU
from src.sigmoid import plot_sigmoid  # Función para graficar la función sigmoide

def main():

    plot_relu()
    plot_sigmoid()

if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente