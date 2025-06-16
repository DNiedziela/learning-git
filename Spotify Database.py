
# Importy
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3

# Dane Spotify
CLIENT_ID = 'XXXXX'
CLIENT_SECRET = 'XXXXXX'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'

# Zakresy i API
scope = 'playlist-read-private user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

# Połączenie z bazą SQLite
conn = sqlite3.connect('spotify.db')
c = conn.cursor()

# Stworzenie tabel
c.execute('''
CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT PRIMARY KEY,
    name TEXT
)''')

c.execute('''
CREATE TABLE IF NOT EXISTS albums (
    album_id TEXT PRIMARY KEY,
    name TEXT,
    release_date TEXT,
    artist_id TEXT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
)''')

c.execute('''
CREATE TABLE IF NOT EXISTS tracks (
    track_id TEXT PRIMARY KEY,
    name TEXT,
    album_id TEXT,
    duration_ms INTEGER,
    popularity INTEGER,
    explicit BOOLEAN,
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
)''')

c.execute('''
CREATE TABLE IF NOT EXISTS playlists (
    playlist_id TEXT PRIMARY KEY,
    name TEXT
)''')

c.execute('''
CREATE TABLE IF NOT EXISTS playlist_tracks (
    playlist_id TEXT,
    track_id TEXT,
    track_order INTEGER,
    PRIMARY KEY (playlist_id, track_id),
    FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id),
    FOREIGN KEY (track_id) REFERENCES tracks(track_id)
)''')

conn.commit()

# Funkcje do wstawiania danych 
def insert_artist(artist):
    c.execute('INSERT OR IGNORE INTO artists (artist_id, name) VALUES (?, ?)',
              (artist['id'], artist['name']))

def insert_album(album, artist_id):
    c.execute('INSERT OR IGNORE INTO albums (album_id, name, release_date, artist_id) VALUES (?, ?, ?, ?)',
              (album['id'], album['name'], album['release_date'], artist_id))

def insert_track(track, album_id):
    c.execute('INSERT OR IGNORE INTO tracks (track_id, name, album_id, duration_ms, popularity, explicit) VALUES (?, ?, ?, ?, ?, ?)',
              (track['id'], track['name'], album_id, track['duration_ms'], track.get('popularity', 0), track['explicit']))

def insert_playlist(playlist):
    c.execute('INSERT OR IGNORE INTO playlists (playlist_id, name) VALUES (?, ?)',
              (playlist['id'], playlist['name']))

def insert_playlist_track(playlist_id, track_id, track_order):
    c.execute('INSERT OR IGNORE INTO playlist_tracks (playlist_id, track_id, track_order) VALUES (?, ?, ?)',
              (playlist_id, track_id, track_order))

conn.commit()

# Pobranie playlist
playlists = sp.current_user_playlists()

for playlist in playlists['items']:
    print(f"Pobieram playlistę: {playlist['name']}")
    insert_playlist(playlist)
    
    results = sp.playlist_tracks(playlist['id'])
    
    track_order = 0
    for item in results['items']:
        track = item['track']
        if track is None:
            continue
        
        # Wstaw artystów 
        first_artist = track['artists'][0]
        insert_artist(first_artist)
        
        # Wstaw album
        album = track['album']
        insert_album(album, first_artist['id'])
        
        # Wstaw utwór
        insert_track(track, album['id'])
        
        # Powiąż utwór z playlistą
        insert_playlist_track(playlist['id'], track['id'], track_order)
        track_order += 1

    conn.commit()

# Update nazwy playlisty
c.execute("""
    UPDATE playlists
    SET name = 'Utwory do testowania stereo - Akustyka Będzin'
    WHERE name = 'Odsłuch'
""")

# Funkcja do usuwania playlist
def delete_playlist_by_name(name):
    c.execute("SELECT playlist_id FROM playlists WHERE name = ?", (name,))
    result = c.fetchone()
    if result:
        playlist_id = result[0]
        c.execute("DELETE FROM playlist_tracks WHERE playlist_id = ?", (playlist_id,))
        c.execute("DELETE FROM playlists WHERE playlist_id = ?", (playlist_id,))
        print(f"Usunięto playlistę '{name}'.")
    else:
        print(f"Nie znaleziono playlisty '{name}'.")
    conn.commit()


# Usunięcie playlisty Hello Kitty

delete_playlist_by_name("Hello Kitty ")
conn.commit()

# Wykaz playlist
c.execute("SELECT * FROM playlists")
for row in c.fetchall():
    print(row)

conn.commit()


conn.close()
print("Import zakończony!")


