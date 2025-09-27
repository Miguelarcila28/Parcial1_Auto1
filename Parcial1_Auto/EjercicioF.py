import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

artist_streams= {}
for i in df['artist_count'].unique():
    artist_streams[i]=[df[df['artist_count']==i].streams]
     
[x for x in artist_streams.values()]     
plt.boxplot([x for x in artist_streams.values()], labels=[x for x in artist_streams.keys()])
plt.xlabel('Artist_count')
plt.ylabel('Streams')
plt.title('Artist_count vs Streams')
plt.show()