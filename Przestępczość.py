import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('fatal-police-shootings-data.csv')

tabela = pd.pivot_table(
    df,
    index='race',
    columns='signs_of_mental_illness',
    values='id',
    aggfunc='count')

tabela['mental_illness_percentage'] = (tabela[True] / (tabela[True] + tabela[False])) * 100
tabela['mental_illness_percentage'] = tabela['mental_illness_percentage'].round(1)

max_value = tabela['mental_illness_percentage'].max()
max_value_race = tabela.index[tabela['mental_illness_percentage'] == max_value]


df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.day_name()

how_many = df['weekday'].value_counts()
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
how_many = how_many.reindex(order)

how_many.plot(kind='bar')
plt.title('Interwencje wg dnia tygodnia')
plt.xlabel('Dzień tygodnia')
plt.ylabel('Liczba wystąpień')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

population = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population')
pop_table = population[0]
pop_table = pop_table[['State', 'Census population, April 1, 2020 [1][2]', 'Census population, April 1, 2010 [1][2]']]
pop_table = pop_table.rename(columns={
    'Census population, April 1, 2020 [1][2]': 'population_2020',
    'Census population, April 1, 2010 [1][2]': 'population_2010'
})
pop_table['est_population_2015'] = ((pop_table['population_2020'] + pop_table['population_2010']) / 2).round(0).astype(int)
pop_table['est_pop_mean'] = ((pop_table['population_2020'] + pop_table['est_population_2015']) / 2).round(0).astype(int)
pop_table = pop_table.iloc[:-4]

abbrv = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._state_abbreviations')
abbrv_table = abbrv[0]
abbrv_table = abbrv_table.iloc[2:]
abbrv_table = abbrv_table.rename(columns={
    0: 'Abbreviation',
    1: 'State'})


new_df = df.groupby('state').size().to_frame('count')
new_df = new_df.merge(abbrv_table, on='Abbreviation', how='left')
new_df = new_df.merge(pop_table[['State', 'est_pop_mean']], on='State', how='left')
new_df = new_df[['Abbreviation', 'State', 'count', 'est_pop_mean']]
new_df['cases_per_1000'] = (new_df['count'] / new_df['est_pop_mean']) * 1000

print(df)
print(abbrv_table)
print(pop_table)
print(new_df)
