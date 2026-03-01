Docstring for kwargs.tracklist
Tracklist
Report a typo

Joe defined a dictionary listing his favorite artists, their albums, and the song from each of the albums. It looks as follows:

tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love"}}

Joe's tastes can change, though.

Your task is to define a tracklist() function that would take several keyword arguments representing musicians and dictionaries with albums and songs as values. For the example above, the call of this function will look as follows:

tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love"})

The function should print the values from the dictionary in the following form:

Woodkid
ALBUM: The Golden Age TRACK: Run Boy Run
ALBUM: On the Other Side TRACK: Samara
Cure
ALBUM: Disintegration TRACK: Lovesong
ALBUM: Wish TRACK: Friday I'm in love

Avoid extra spaces. You do not need to call a function, just implement it.
Hint by
User 28092587 avatar
User 28092587
There is a dictionary of a dictionary. So, Use .items for both loops and pull out the stuff! :)