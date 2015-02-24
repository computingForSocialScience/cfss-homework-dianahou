import sys
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *
import networkx as networkx
import pandas as pd
import random
from io import open

if __name__ == '__main__':
    artist_names = sys.argv[1:]

artists_ids_list = []
for name in artist_names:
    artistID = fetchArtistId(name)
    artists_ids_list.append(artistID)

edgeLists = [] #list of edge lists for different artists
#for artistID in artists_ids_list:
for i in range(len(artists_ids_list)):
    edgeList = getEdgeList(artists_ids_list[i], 2)
    edgeLists.append(edgeList)

combined_EdgeLists = edgeLists[0] #the first edgelist!
for i in range(len(edgeLists)):
    combined_EdgeLists = combineEdgelists(combined_EdgeLists, edgeLists[i]) #adding edgeList to combined list
combined_EdgeLists.columns = ['artist1', 'artist2']

#print combined_EdgeLists

g = pandasToNetworkX(combined_EdgeLists)

artist_sample = []
for i in range(30):
    artist_sample.append(randomCentralNode(g))

artist_names = []
album_list = []
for artistID in artist_sample:
    artistName = fetchArtistInfo(artistID)['name']
    artist_names.append(artistName)
    albumIdList = fetchAlbumIds(artistID) #album id list for each artist
    randomAlbum = (random.choice(albumIdList))
    randomAlbumName = fetchAlbumInfo(randomAlbum)['name']
    album_list.append((randomAlbumName, randomAlbum))

random_tracks = []
for album in album_list:
    url = "https://api.spotify.com/v1/albums/" + album[1] + "/tracks"
    req = requests.get(url)
    trackData = req.json().get('items')
    trackList = []
    for i in range(len(trackData)):
        trackName = trackData[i]['name']
        trackList.append(trackName)
        randomTrack = (random.choice(trackList))
    random_tracks.append(randomTrack)

print random_tracks

f = open('playlist.csv', 'w')
f.write(u'artist_name, album_name, track_name\n')
for i in range(len(random_tracks)):
    artistName = artist_names[i]
    albumName = album_list[i][0]
    trackName = random_tracks[i]
    f.write('"' + artistName + '"' + ',' + '"' + albumName + '"' + ',' + '"' + trackName + '"' + '\n')
f.close()







