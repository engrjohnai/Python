

def tracklist(**musicians):
    for artist, albums in musicians.items():
        print(artist)
        for albums, tracks in albums.items():
            print(f"ALBUM: {albums} TRACK: {tracks}")
        
tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love"}}

tracklist(**tracks)