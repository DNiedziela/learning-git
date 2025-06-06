

import unicodedata

import random

library = []

class Movie:
    
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views
        library.append(self)

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self):
        self.views += 1

class Series(Movie):
    def __init__(self, title, year, genre, views, season, episode):
        super().__init__(title, year, genre, views)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"
    
movies_data = [
    ("Inception", 2010, "Sci-Fi", 1500000),
    ("The Godfather", 1972, "Crime", 2300000),
    ("Pulp Fiction", 1994, "Crime", 1800000),
    ("The Dark Knight", 2008, "Action", 2500000),
    ("Forrest Gump", 1994, "Drama", 1600000),
    ("The Matrix", 1999, "Sci-Fi", 2000000),
    ("Interstellar", 2014, "Sci-Fi", 2100000),
    ("Fight Club", 1999, "Drama", 1700000),
    ("Parasite", 2019, "Thriller", 1900000),
    ("Whiplash", 2014, "Drama", 1400000),
]

series_data = [
    ("Breaking Bad", 2008, "Crime", 3500000, 5, 14),
    ("Stranger Things", 2016, "Sci-Fi", 4000000, 3, 8),
    ("Game of Thrones", 2011, "Fantasy", 5000000, 8, 6),
    ("The Office", 2005, "Comedy", 2700000, 7, 24),
    ("Sherlock", 2010, "Crime", 2200000, 4, 3),
]


def get_movies():
    return sorted(
        [item for item in library if type(item) == Movie],
        key=lambda x: x.title)

def get_series():
    return sorted(
        [item for item in library if type(item) == Series],
        key=lambda x: x.title)

for title, year, genre, views in movies_data:
    Movie(title, year, genre, views)

for title, year, genre, views, season, episode in series_data:
    Series(title, year, genre, views, season, episode)


def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    return text

def search():
    query = input("Wpisz czego szukasz: ")
    query_norm = normalize_text(query)
    results = [item for item in library if query_norm in normalize_text(item.title)]
    if results:
        print("Znalezione tytuły:")
        for item in results:
            print(item)
    else:
        print("Brak wyników.")
    return results



def generate_views():
    random_number = random.randint(1, 100)
    item = random.choice(library)
    item.views += random_number

def generate10():
    for _ in range(10):
        generate_views()

def top_titles():
    return sorted(library, key=lambda x: x.views, reverse=True)[:10]

movies = get_movies()
print("\n Filmy w bibliotece: \n")
for movie in movies:
    print(movie)

series = get_series()
print("\n Seriale w bibliotece: \n")
for serie in series:
    print(serie)


generate10()

print("\n \n Top 10 najpopularniejszych tytułów:\n")
for item in top_titles():
    print(f"{item} — {item.views} wyświetleń")

print("\n")

search()