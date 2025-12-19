import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from datetime import datetime
import glob
import os
import json
import pickle
import six
sns.set()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.mode.chained_assignment = None

csv= "C:\\Users\\Joao\\analise de dados\\daily_trending_videos.csv"
df = pd.read_csv(csv, sep=";", encoding="latin1")



df['video_id'] = df['video_id'].astype('string')
df['title'] = df['title'].astype('string')
df['channel'] = df['channel'].astype('string')
df['country'] = df['country'].astype('category')
df['views'] = pd.to_numeric(df['views'], errors='coerce').astype('Int64')
df['likes'] = pd.to_numeric(df['likes'], errors='coerce').astype('Int64')
df['comments'] = pd.to_numeric(df['comments'], errors='coerce').astype('Int64')
df['published_at'] = pd.to_datetime(df['published_at'], utc=True, errors='coerce')
df['fetch_date'] = pd.to_datetime(df['fetch_date'], format='%d/%m/%Y %H:%M', errors='coerce')

df.set_index('video_id', inplace=True)

sns.heatmap(df.isnull(), cbar=False)
plt.figure()

df_br = df[df['country'] == 'BR']

views_por_canal = (df_br.groupby('channel')['views'].sum().sort_values(ascending=False))
views_por_canal.head(10).plot(kind='barh',figsize=(10, 6))
plt.title('Top 10 canais com mais visualizações do Brasil')
plt.xlabel('Total de visualizações')
plt.ylabel('Canal')
plt.gca().invert_yaxis()
plt.show()

likes_por_canal = (df_br.groupby('channel')['likes'].sum().sort_values(ascending=False))
likes_por_canal.head(10).plot(kind='barh',figsize=(10, 6))
plt.title('Top 10 canais com mais likes do Brasil')
plt.xlabel('Total de likes')
plt.ylabel('Canal')
plt.gca().invert_yaxis()
plt.show()

df.plot.scatter(x='views', y='likes', alpha=0.5)
plt.title('Likes vs Views')
plt.show()

df_br.plot.scatter(x='views', y='likes', alpha=0.5)
plt.title('Likes vs Views')
plt.show()
