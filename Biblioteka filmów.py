



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
    

def get_movies():
    return sorted(
        [item for item in library if type(item) == Movie],
        key=lambda x: x.title)

def get_series():
    return sorted(
        [item for item in library if type(item) == Series],
        key=lambda x: x.title)

for title, year, genre, views in library:
    Movie(title, year, genre, views)

import unicodedata

def search():
    query = input("Wpisz czego szukasz: ")
    query_norm = normalize_text(query)
    results = []
    for item in library:
        title_norm = normalize_text(item.title)
        if query_norm in title_norm:  
            results.append(item)
    return results

import random

def generate_views():
    random_number = random.randint(1, 100)
    item = random.choice(library)
    item.views += random_number

def generate10():
    for _ in range(10):
        generate_views

def top_titles():
    return sorted(library, key=lambda x: x.views, reverse=True)[:10]




