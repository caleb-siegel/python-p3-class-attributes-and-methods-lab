class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_artists()
        self.add_to_genres()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        Song.count += 1
    
    def add_to_artists(self):
        if not self.artist in Song.artists:
            Song.artists.append(self.artist)
    
    def add_to_genres(self):
        if not self.genre in Song.genres:
            Song.genres.append(self.genre)
    
    def add_to_genre_count(self):
        if not self.genre in list(Song.genre_count):
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1
    
    def add_to_artist_count(self):
        if not self.artist in list(Song.artist_count):
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
ninety_eight_problems = Song("98 Problems", "Beyonce", "Rock")
hundred_problems = Song("100 Problems", "Jay-Z", "Rap")
hundred_problems = Song("100 Problems", "Jay-Z", "Rap")
hundred_problems = Song("100 Problems", "Jay-Cole", "Rap")
hundred_problems = Song("100 Problems", "Jay-Z", "Rap")

print(Song.genre_count)
print(Song.artist_count)