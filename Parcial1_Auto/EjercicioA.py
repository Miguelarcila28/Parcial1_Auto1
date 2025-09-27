import pandas as pd
import numpy as np

df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

# Contar variables categóricas (object)
cat = df.select_dtypes(include='object').shape[1]
# Contar variables numéricas
num = df.select_dtypes(include='number').shape[1]

print("Variables categóricas:", cat)
print("Variables numéricas:", num)