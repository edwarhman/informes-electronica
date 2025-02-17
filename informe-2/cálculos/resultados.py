import numpy as np
from sympy import symbols, diff, Abs, log, N
import math
import pandas as pd
import sys
from incertidumbres import evaluar_funcion, calc_error_absoluto, calc_desviacion_estandar, agregar_calculo_a_dataframe, calcular_medicion_indirecta


def calcular_ganancia(datos, columnas):
    vi, vo = symbols('vi, vo')
    func_ganancia = (vo/vi)
    agregar_calculo_a_dataframe(datos, func_ganancia, [vi, vo], columnas, 'Ganancia')

def calcular_frecuencia(datos, columnas):
    T = symbols('T')
    func_frecuencia = 1/T
    agregar_calculo_a_dataframe(datos, func_frecuencia, [T], columnas, 'Frecuencia')

def calcular_corriente_ley_ohm(datos, columnas, titulo):
    vo, rl = symbols('vo rl')
    func_corriente_ley_ohm = vo/rl
    agregar_calculo_a_dataframe(datos, func_corriente_ley_ohm, [vo, rl], columnas, titulo) 

def calcular_tension_offset(datos, columnas):
    vo, rf, rs = symbols('vo rf rs')
    func_tension_offset = (rs/rf) * vo
    agregar_calculo_a_dataframe(datos, func_tension_offset, [vo, rf, rs], columnas, 'Tensión de offset')

def calcular_corriente_b1(datos, columnas):
    vo, rf, rs, rb, vos = symbols('vo rf rs rb vos')
    func_corriente_b1 = (vos*(1 + rf/rs) - vo)/(rb*(1 + rf/rs))
    agregar_calculo_a_dataframe(datos, func_corriente_b1, [vo, rf, rs, rb, vos], columnas, 'Corriente B1')

def calcular_corriente_b2(datos, columnas):
    vo, rf, rs, rb, vos = symbols('vo rf rs rb vos')
    func_corriente_b2 = (vo - vos*(1 + rf/rs))/(rb*(1 + rf/rs))
    agregar_calculo_a_dataframe(datos, func_corriente_b2, [vo, rf, rs, rb, vos], columnas, 'Corriente B2')

def calcular_corriente_bias(datos, columnas):
    Ib1, Ib2 = symbols('Ib1, Ib2')
    func_corriente_bias = Ib1 - Ib2
    agregar_calculo_a_dataframe(datos, func_corriente_bias, [Ib1, Ib2], columnas, 'Corriente Bias')

def calcular_producto_ganancia_ancho_de_banda(datos, columnas):
    A, Wl, Wh = symbols('A, Wl, Wh')
    func_producto_ganancia_ancho_de_banda = A * (Wh - Wl)
    agregar_calculo_a_dataframe(datos, func_producto_ganancia_ancho_de_banda, [A, Wl, Wh], columnas, 'Producto Ganancia Ancho de Banda')

def calcular_slew_rate(datos, columnas):
    vo, t = symbols('vo t')
    func_slew_rate = vo / t
    agregar_calculo_a_dataframe(datos, func_slew_rate, [vo, t], columnas, 'Slew Rate')

def calcular_regulacion_de_voltaje(datos, columnas):
    vsc, vcc = symbols('vsc, vcc')
    func_regulacion_de_voltaje = (vsc - vcc)*100/vcc
    agregar_calculo_a_dataframe(datos, func_regulacion_de_voltaje, [vcc, vsc], columnas, 'Regulación de voltaje')

df_ganancia_frecuencia = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0)

calcular_ganancia(df_ganancia_frecuencia, [2,3,4,5])
calcular_frecuencia(df_ganancia_frecuencia, [6,7])

df_corriente_convertidor_tension_a_corriente = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Fuente de corriente')
calcular_corriente_ley_ohm(df_corriente_convertidor_tension_a_corriente, [2,3,4,5], 'Corriente fuente de corriente')
df_tension_offset = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Tensión Offset')
df_corriente_bias = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Corriente Bias')

calcular_tension_offset(df_tension_offset, [2,3,4,5,6,7])

# Seleccionar la primera fila de df_corriente_b1
df_corriente_b1 = df_corriente_bias.loc[[0]]
df_corriente_b2 = df_corriente_bias.loc[[1]]

calcular_corriente_b1(df_corriente_b1, [2,3,4,5,6,7,8,9,10,11])
calcular_corriente_b2(df_corriente_b2, [2,3,4,5,6,7,8,9,10,11])

# Create a new dataframe with the merged bias currents
df_corriente_bias_merged = pd.DataFrame()
df_corriente_bias_merged['Corriente B1'] = df_corriente_b1['Corriente B1'].values
df_corriente_bias_merged['ΔCorriente B1'] = df_corriente_b1['ΔCorriente B1'].values
df_corriente_bias_merged['Corriente B2'] = df_corriente_b2['Corriente B2'].values 
df_corriente_bias_merged['ΔCorriente B2'] = df_corriente_b2['ΔCorriente B2'].values

# Calculate the bias current using the merged data
print(df_corriente_bias_merged)
calcular_corriente_bias(df_corriente_bias_merged, [0,1,2,3])

df_producto_ganancia_ancho_de_banda = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='ganancia ancho de banda')
calcular_producto_ganancia_ancho_de_banda(df_producto_ganancia_ancho_de_banda, [2,3,4,5,6,7])

df_slew_rate = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Slew Rate')
calcular_slew_rate(df_slew_rate, [2,3,4,5])

df_corriente_cortocircuito = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Corriente de cortocircuito')
calcular_corriente_ley_ohm(df_corriente_cortocircuito, [2,3,4,5], 'Corriente de cortocircuito')

df_fuente_de_corriente_variable = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Fuente de corriente variable')
calcular_corriente_ley_ohm(df_fuente_de_corriente_variable, [2,3,4,5], 'Fuente de corriente variable')

df_regulacion_de_voltaje = pd.read_excel('./Electrónica II - Informe 2.xlsx', header=0, sheet_name='Regulación de voltaje')
calcular_regulacion_de_voltaje(df_regulacion_de_voltaje, [2,3,4,5])

v2, v1 = symbols('v2, v1')
func_diferencia_de_tension = v2 - v1
diferencia_de_tension = calcular_medicion_indirecta(func_diferencia_de_tension, [v2, v1], datos=[[1, 0.5], [0.2, 0.1]])
print(diferencia_de_tension)


try:
    with pd.ExcelWriter('Electrónica II - Informe 2 cálculos.xlsx') as writer:
        df_ganancia_frecuencia.to_excel(writer, sheet_name='Ganancia')
        df_corriente_convertidor_tension_a_corriente.to_excel(writer, sheet_name='Fuente de corriente') 
        df_tension_offset.to_excel(writer, sheet_name='Tensión Offset')
        df_corriente_b1.to_excel(writer, sheet_name='Corriente B1')
        df_corriente_b2.to_excel(writer, sheet_name='Corriente B2')
        df_corriente_bias_merged.to_excel(writer, sheet_name='Corriente Bias')  
        df_producto_ganancia_ancho_de_banda.to_excel(writer, sheet_name='ganancia ancho de banda')
        df_slew_rate.to_excel(writer, sheet_name='Slew Rate')
        df_corriente_cortocircuito.to_excel(writer, sheet_name='Corriente de cortocircuito')
        df_fuente_de_corriente_variable.to_excel(writer, sheet_name='Fuente de corriente variable')
        df_regulacion_de_voltaje.to_excel(writer, sheet_name='Regulación de voltaje')
except FileNotFoundError:
    # If file doesn't exist, create it with mode='w'
    print('File not found, creating it')
    with pd.ExcelWriter('Electrónica II - Informe 2 cálculos.xlsx', mode='w') as writer:
        df_ganancia_frecuencia.to_excel(writer, sheet_name='Ganancia') 
        df_corriente_convertidor_tension_a_corriente.to_excel(writer, sheet_name='Fuente de corriente') 
        df_tension_offset.to_excel(writer, sheet_name='Tensión Offset')
        df_corriente_bias_merged.to_excel(writer, sheet_name='Corriente Bias')
        df_producto_ganancia_ancho_de_banda.to_excel(writer, sheet_name='ganancia ancho de banda')
        df_slew_rate.to_excel(writer, sheet_name='Slew Rate')
        df_corriente_cortocircuito.to_excel(writer, sheet_name='Corriente de cortocircuito')
        df_fuente_de_corriente_variable.to_excel(writer, sheet_name='Fuente de corriente variable')
        df_regulacion_de_voltaje.to_excel(writer, sheet_name='Regulación de voltaje')
except ValueError as e:
    print(e)