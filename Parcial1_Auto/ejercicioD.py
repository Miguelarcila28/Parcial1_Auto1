import pandas as pd

df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

def canciones_por_artista(df, a):
    return df[df['artist(s)_name'] == a]

a = input("Ingrese el nombre del artista: ")

canciones = canciones_por_artista(df, a)
print(canciones)

