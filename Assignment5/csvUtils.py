from io import open
from fetchArtist import *
from fetchAlbums import *
import csv

artist_info_list = []
artist_info_list.append(fetchArtistInfo(fetchArtistId('beyonce')))
artist_info_list.append(fetchArtistInfo(fetchArtistId('lauryn hill')))
artist_info_list.append(fetchArtistInfo(fetchArtistId('paul simon')))
#print artist_info_list


def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """
    
    f = open('artists.csv', 'w')
    f.write(u'ARTIST_ID, ARTIST_NAME, ARTIST_FOLLOWERS, ARTIST_POPULARITY\n')
    for artist in artist_info_list:
        artistIndex = artist_info_list.index(artist)
        ID = artist_info_list[artistIndex]["id"]
        name = artist_info_list[artistIndex]["name"]
        followers = artist_info_list[artistIndex]["followers"]
        popularity = artist_info_list[artistIndex]["popularity"]

        #line = u'%s, "%s", %d, %d\n' %  (ID, name, followers, popularity)
        f.write(ID + "," + '"'+name+'"' +","+str(followers)+","+str(popularity) + '\n')
    f.close()



#print fetchAlbumIds(fetchArtistId('paul simon'))
#print fetchAlbumIds(fetchArtistId('beyonce'))

album_info_list = []
album_info_list.append(fetchAlbumInfo(u'4Scv3lrqPGBbpjjVPaDG4B'))
album_info_list.append(fetchAlbumInfo(u'46MJtyvpieCwQ4U6R5wNmw'))
album_info_list.append(fetchAlbumInfo(u'3BgJSYve7Hvp80NZ6JWTmK'))
album_info_list.append(fetchAlbumInfo(u'2UJwKSBUz6rtW4QLK74kQu'))
album_info_list.append(fetchAlbumInfo(u'6KPiNRUaPSuFVes2xEUjYk'))
#print album_info_list

      
def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """
    g = open('albums.csv', 'w')
    g.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
    for album in album_info_list:
        #albumIndex = album_info_list.index(album)
        artist_id = album["artist_id"]
        album_id = album["album_id"]
        album_name = album["name"]
        album_year = album["year"]
        album_popularity = album["popularity"]
        
        g.write(artist_id + "," + album_id +","+ '"'+album_name+'"' +","+str(album_year)+","+str(album_popularity) + '\n')
    g.close()



if __name__ == '__main__':
    writeArtistsTable(artist_info_list)
    writeAlbumsTable(album_info_list)
    




