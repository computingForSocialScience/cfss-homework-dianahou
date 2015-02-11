import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    url = "https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    req = requests.get(url)
    artist_data = req.json()
    '''The value to the key "items" is a dictionary within a list. [0] indexes into the list'''
    artist_id = artist_data["artists"]["items"][0]["id"]
    return artist_id

print fetchArtistId('Tania Bowra')


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id
    req = requests.get(url)
    artist_data = req.json()
    '''Defining dictionary'''
    artist_dict = {}
    artist_dict['followers'] = artist_data["followers"]["total"]
    artist_dict['genres'] = artist_data["genres"]
    artist_dict['id'] = artist_id
    artist_dict['name'] = artist_data["name"]
    artist_dict['popularity'] = artist_data["popularity"]
    return artist_dict

print fetchArtistInfo(fetchArtistId('beyonce'))

