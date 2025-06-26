from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, ForeignKey
import csv

# Połączenie z bazą danych
engine = create_engine('sqlite:///clean_database.db', echo=True)
metadata = MetaData()

# Definicja tabeli stations
stations = Table(
    'stations', metadata,
    Column('station', String, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)

# Definicja tabeli measurements
measurements = Table(
    'measurements', metadata,
    Column('station', String, ForeignKey('stations.station'), primary_key=True),
    Column('date', String, primary_key=True),
    Column('precip', Float),
    Column('tobs', Float)
)

# Tworzenie tabel
metadata.create_all(engine)

# Funkcja do wstawiania danych z pliku CSV do podanej tabeli
def insert_data_from_csv(table, csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]

    with engine.begin() as conn:
        conn.execute(table.insert(), rows)

# Wstawianie danych
insert_data_from_csv(stations, 'clean_stations.csv')
insert_data_from_csv(measurements, 'clean_measure.csv')

# Testowy SELECT
with engine.connect() as conn:
    results = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    for row in results:
        print(row)
