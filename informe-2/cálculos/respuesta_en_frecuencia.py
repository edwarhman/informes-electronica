import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

df = pd.read_excel('./filtro-sallen-key.xlsx', header=0)


# Convert the DataFrame to a NumPy array
data_array = df.to_numpy()
data_array.sort

# Select rows 13 to 20 (inclusive) and columns from index 3 onwards
datos_filtro = data_array  # Selecting columns 9 and 11 (zero-based indexing)
datos_filtro_ordenado = datos_filtro[datos_filtro[:, 1].argsort()]


def graficar_respuesta_en_frecuencia(datos, titulo):
    magnitud = datos[:, 0]
    frecuencia = datos[:, 1]

    plt.figure(figsize=(10, 5))
    
    # Configurar escala logarítmica para el eje x
    plt.semilogx(frecuencia, magnitud, 'b-', label='Respuesta en frecuencia')
    
    # Añadir etiquetas y título
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    
    # Guardar la figura
    plt.savefig(titulo + '.png', dpi=300, bbox_inches='tight')
    plt.close()

graficar_respuesta_en_frecuencia(datos_filtro_ordenado, 'Respuesta en frecuencia - Filtro Sallen-Key')
