import pandas as pd
import numpy as np

df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

# Filtro
artistas = ['Taylor Swift', 'Coldplay']
df_filtrado = df[df['artist(s)_name'].isin(artistas)]

# Contar canciones por artista
tabla = df_filtrado.groupby('artist(s)_name').size().reset_index(name='cantidad_canciones')

print(tabla)
