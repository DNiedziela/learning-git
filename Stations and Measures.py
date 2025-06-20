

from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, ForeignKey
import csv

engine = create_engine('sqlite:///clean_database.db', echo=True)
metadata = MetaData()

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

measurements = Table(
    'measurements', metadata,
    Column('station', String, ForeignKey('stations.station'), primary_key=True),
    Column('date', String, primary_key=True),  
    Column('precip', Float),
    Column('tobs', Float)
)


with open('clean_stations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with engine.connect() as conn:
    conn.execute(stations.insert(), rows)
    conn.commit()


with open('clean_measures.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with engine.connect() as conn:
    conn.execute(measures.insert(), rows)
    conn.commit()



with engine.connect() as conn:
    results = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    print(results)



metadata.create_all(engine)












with engine.connect() as conn:
    results = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    print(results)

