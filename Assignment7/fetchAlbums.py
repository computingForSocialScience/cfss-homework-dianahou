import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/albums?market=US&album_type=album"
    req = requests.get(url)
    album_data = req.json()
    album_ids = []
    '''Items is a dictionary key. Its value is a list of dictionaries. Each of these dictionaries contains
    info for one album. Each dictionary has an "id" key.'''
    for album in album_data["items"]:
        albumIndex = album_data["items"].index(album)
        albumID = album_data["items"][albumIndex]["id"]
        album_ids.append(albumID)
    return album_ids







def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url = "https://api.spotify.com/v1/albums/" + album_id
    req = requests.get(url)
    album_info = req.json()
    '''Defining dictionary'''
    album_dict = {}
    album_dict['artist_id'] = album_info["artists"][0]["id"]
    album_dict['album_id'] = album_id
    album_dict['name'] = album_info["name"]
    album_dict['year'] = album_info["release_date"][0:4]
    album_dict['popularity'] = album_info["popularity"]
    return album_dict



if __name__ == '__main__':
    print fetchAlbumIds('1vCWHaC5f2uS3yhpwWbIA6')
    print fetchAlbumInfo('0sNOF9WDwhWunNAHPD3Baj')


