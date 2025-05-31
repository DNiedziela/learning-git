library = [
    ("Skazani na Shawshank", 1994, "Dramat", 10954716),
    ("Zielona mila", 1999, "Dramat", 1029786),
    ("Nietykalni", 2011, "Biograficzny / Dramat / Komedia", 702600),
    ("Ojciec chrzestny", 1972, "Dramat / Gangsterski", 566074),
    ("Dwunastu gniewnych ludzi", 1957, "Dramat sądowy", 236359),
    ("Forrest Gump", 1994, "Dramat / Komedia", 1020115),
    ("Lot nad kukułczym gniazdem", 1975, "Dramat / Psychologiczny", 424576),
    ("Ojciec chrzestny II", 1974, "Dramat / Gangsterski", 288332),
    ("Władca Pierścieni: Powrót króla", 2003, "Fantasy / Przygodowy", 547327),
    ("Lista Schindlera", 1993, "Dramat / Wojenny", 373662),
    ("Pulp Fiction", 1994, "Dramat / Gangsterski", 1012345),
    ("Władca Pierścieni: Drużyna Pierścienia", 2001, "Fantasy / Przygodowy", 523456),
    ("Władca Pierścieni: Dwie wieże", 2002, "Fantasy / Przygodowy", 512789),
    ("Fight Club", 1999, "Dramat / Thriller", 987654),
    ("Incepcja", 2010, "Sci-Fi / Thriller", 876543),
    ("Matrix", 1999, "Sci-Fi / Akcja", 765432),
    ("Gladiator", 2000, "Dramat / Historyczny", 654321),
    ("Se7en", 1995, "Thriller / Kryminał", 543210),
    ("Milczenie owiec", 1991, "Thriller / Kryminał", 432109),
    ("Leon zawodowiec", 1994, "Dramat / Akcja", 321098),
    ("Titanic", 1997, "Dramat / Romans", 210987),
    ("Braveheart: Waleczne serce", 1995, "Dramat / Historyczny", 198765),
    ("American History X", 1998, "Dramat", 187654),
    ("Życie jest piękne", 1997, "Dramat / Komedia", 176543),
    ("Requiem dla snu", 2000, "Dramat / Psychologiczny", 165432),
    ("Pianista", 2002, "Dramat / Wojenny", 154321),
    ("Zielona książka", 2018, "Biograficzny / Dramat / Komedia", 143210),
    ("Joker", 2019, "Dramat / Kryminał", 132109),
    ("Parasite", 2019, "Dramat / Thriller", 121098),
    ("Whiplash", 2014, "Dramat / Muzyczny", 110987),
    ("Interstellar", 2014, "Sci-Fi / Dramat", 109876),
    ("Django", 2012, "Western / Dramat", 98765),
    ("Avengers: Koniec gry", 2019, "Akcja / Sci-Fi", 87654),
    ("Avengers: Wojna bez granic", 2018, "Akcja / Sci-Fi", 76543),
    ("Strażnicy Galaktyki", 2014, "Akcja / Sci-Fi / Komedia", 65432),
    ("Deadpool", 2016, "Akcja / Komedia", 54321),
    ("Logan: Wolverine", 2017, "Akcja / Dramat", 43210),
    ("Kapitan Ameryka: Wojna bohaterów", 2016, "Akcja / Sci-Fi", 32109),
    ("Iron Man", 2008, "Akcja / Sci-Fi", 21098),
    ("Thor: Ragnarok", 2017, "Akcja / Sci-Fi / Komedia", 10987),
    ("Czarna Pantera", 2018, "Akcja / Sci-Fi", 9876),
    ("Doktor Strange", 2016, "Akcja / Sci-Fi", 8765),
    ("Ant-Man", 2015, "Akcja / Sci-Fi / Komedia", 7654),
    ("Kapitan Marvel", 2019, "Akcja / Sci-Fi", 6543),
    ("Spider-Man: Daleko od domu", 2019, "Akcja / Sci-Fi", 5432),
    ("Spider-Man: Homecoming", 2017, "Akcja / Sci-Fi", 4321),
    ("Strażnicy Galaktyki vol. 2", 2017, "Akcja / Sci-Fi / Komedia", 3210),
    ("Thor: Mroczny świat", 2013, "Akcja / Sci-Fi", 2109),
    ("Iron Man 2", 2010, "Akcja / Sci-Fi", 1098),
    ("Iron Man 3", 2013, "Akcja / Sci-Fi", 987)]






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




