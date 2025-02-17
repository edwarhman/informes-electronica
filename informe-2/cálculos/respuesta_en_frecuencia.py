import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

df = pd.read_excel('./Electrónica II - Informe 2 cálculos.xlsx', header=0)


# Convert the DataFrame to a NumPy array
data_array = df.to_numpy()
data_array.sort

# Select rows 13 to 20 (inclusive) and columns from index 3 onwards
datos_filtro_sallen_key = data_array[12:20, [9,11]]  # Selecting columns 9 and 11 (zero-based indexing)
datos_filtro_sallen_key_ordenado = datos_filtro_sallen_key[datos_filtro_sallen_key[:, 1].argsort()]

datos_filtro_realimentacion_multiple = data_array[20:28, [9,11]]
datos_filtro_realimentacion_multiple_ordenado = datos_filtro_realimentacion_multiple[datos_filtro_realimentacion_multiple[:, 1].argsort()]

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

graficar_respuesta_en_frecuencia(datos_filtro_sallen_key_ordenado, 'Respuesta en frecuencia - Filtro Sallen-Key')
graficar_respuesta_en_frecuencia(datos_filtro_realimentacion_multiple_ordenado, 'Respuesta en frecuencia - Filtro Realimentación Múltiple')
