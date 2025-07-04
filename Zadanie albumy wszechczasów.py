import pandas as pd

tables = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/')

df = tables[0]

df.columns = ['POZ', 'TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']

liczba_artystow = df['ARTYSTA'].nunique()
print(f"Liczba unikalnych artystów: {liczba_artystow}")

top_artysci = df['ARTYSTA'].value_counts()
print(f"Topowe zespoły: \n{top_artysci.head(2)}")

df.columns = [col.capitalize() for col in df.columns]

df = df.drop(0)

df = df.drop('Max poz', axis=1)

albumy_na_rok = df.groupby('Rok').size()
najczestszy_rok = albumy_na_rok.sort_values(ascending=False).index[0]
liczba = albumy_na_rok.max()

print(f"Najwięcej albumów ({liczba}) pochodzi z roku {najczestszy_rok}")

albumy_60_90 = df[(df['Rok'] >= '1960') & (df['Rok'] <= '1990')]
liczba_albumow = len(albumy_60_90)

print(f"Liczba albumów wydanych w latach 1960–1990: {liczba_albumow}")

najmlodszy_rok = df['Rok'].max()
print(f"Najmłodszy album pochodzi z roku {najmlodszy_rok}")

df['Rok'] = pd.to_numeric(df['Rok'])

najwczesniejsze_albumy = df.loc[df.groupby('Artysta')['Rok'].idxmin(), ['Artysta', 'Rok', 'Tytuł']]
print(najwczesniejsze_albumy.reset_index(drop=True))

najwczesniejsze_albumy.to_csv('najwczesniejsze_albumy.csv', index=False)


print(df)