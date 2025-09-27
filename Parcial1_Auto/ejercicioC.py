import numpy as np
import pandas as pd

df= pd.read_csv('spotify-2023.csv', encoding='latin-1')

a= df.columns
print("Nombres de las columnas:", a)

df_max= df.max(numeric_only= True )# Obtener los valores máximos solo de las columnas numéricas
print("Valores máximos de las columnas numéricas:\n", df_max)

df_min= df.min(numeric_only= True)# Obtener los valores mínimos solo de las columnas numéricas
print("Valores mínimos de las columnas numéricas:\n", df_min)   