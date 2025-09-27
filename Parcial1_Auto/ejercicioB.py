import pandas as pd

df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

canciones_coldplay = df[df['artist(s)_name'] == 'Coldplay'].shape[0]   
print("Cantidad de canciones de Coldplay:", canciones_coldplay)