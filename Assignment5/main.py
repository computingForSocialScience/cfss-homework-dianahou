import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    artist_id_list = []
    artist_info_list = []
    for name in artist_names:
        artistId = fetchArtistId(name) #get artistID
        artist_id_list.append(artistId) #append it to the list
        artistInfo = fetchArtistInfo(artistId) #get artistInfo dictionary
        artist_info_list.append(artistInfo) #append it to the artist_info_list

    #album_ids_list = []
    album_info_list = []
    for artistId in artist_id_list:
        albumIds = fetchAlbumIds(artistId) #get list of albumIds
        #album_ids_list.append(albumIds) #append list to album_ids_list
        for albumId in albumIds:   #for each album in one artist's list of album IDs
            albumInfo = fetchAlbumInfo(albumId) #get albumInfo dictionary
            album_info_list.append(albumInfo) #append it to the album_info_list

    writeArtistsTable(artist_info_list)
    writeAlbumsTable(album_info_list)
    plotBarChart()


    

