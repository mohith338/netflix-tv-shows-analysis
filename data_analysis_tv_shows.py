import pandas as pd

df=pd.read_csv(r'C:\Users\User\Desktop\TV Shows - Netflix.csv')
df.head()
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()

df=df.drop_duplicates()

df.columns=df.columns.str.strip().str.lower().str.replace(' ',"_")

df['titles']=df['titles'].fillna('unknown')
df['year']=df['year'].fillna(df['year'].median())
df['rating']=df['rating'].fillna('not rated')
df['netflix']=df['netflix'].fillna('not updated')
df['imdb_rating']=df['imdb_rating'].fillna(df['imdb_rating'].mean())

df['year']=df['year'].astype(int)
df['rating']=df['rating'].astype(str).str.strip()
df['rating']=df['rating'].replace(['','Nan','nan','None','none'], 'not rated')
df['rating']=df['rating'].fillna('Not rated')

titles=df.shape[0]
print("tiles:", titles)

imdb_rating=df['imdb_rating'].mean()
print('imdb_rating:',imdb_rating)

top_rated=df.sort_values(by=['imdb_rating'],ascending=False).head(10)
print(top_rated[['titles','year','rating','imdb_rating']])

lower_rated=df.sort_values(by=['imdb_rating'],ascending=True).head(10)
print(lower_rated[['titles','year','rating','imdb_rating']])

show_by_year=df['year'].value_counts().sort_index()
print(show_by_year)



show_by_rating=df['rating'].value_counts()
print(show_by_rating)

import matplotlib.pyplot as plt
show_by_year.plot(kind='line')
plt.title('netflix shows by year')
plt.xlabel('year')
plt.ylabel('number of shows')
plt.show()

show_by_rating.plot(kind='bar')
plt.title('netflix shows by rating')
plt.xlabel('rating')
plt.ylabel('number of shows')
plt.show()

top_rated.plot(x='titles',y='imdb_rating',kind='bar')
plt.title('netflix shows by top rated')
plt.xlabel('rating')
plt.ylabel('number of shows')
plt.xticks(rotation=45)
plt.show()


df.to_csv('cleanned_netflix_tv_shows_dataset.csv', index=False)
print('succesfully')
import os
print('location')
print(os.getcwd())

import sqlite3
conn=sqlite3.connect('netflix_data.db')
df.to_sql('netflix_analysis', conn, if_exists='replace', index=False)
conn.close()
print('done')

