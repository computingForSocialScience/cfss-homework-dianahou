import sys
import requests
import csv
import pandas as pd
import numpy as np


def getRelatedArtists(artistID):
    '''Returns a list of related artist ids'''
    url = "https://api.spotify.com/v1/artists/" + artistID + "/related-artists"
    req = requests.get(url)
    related_artist_data = req.json()
    #dictionary value to "artists" is a list of dictionaries. each dictionary is a related artist
    relatedArtistIdList = []
    for related_artist in related_artist_data["artists"]:
        relatedArtistId = related_artist["id"]
        relatedArtistIdList.append(relatedArtistId)
    return relatedArtistIdList

#print getRelatedArtists('43ZHCT0cAZBISjO8DG9PnE')

def getDepthEdges(artistID, depth):
    '''Returns list of tuples representing pairs of related artists according to specified depth'''
    depthEdgesList = [] #master list of tuples
    depthEdgesList_checked = [] #master list of tuples checked for duplicates
    relatedArtists = []
    relatedArtists.append(artistID) # at 0 depth, we have original artist ID in relatedArtists list
    for i in range(depth):
        for relatedArtistId in relatedArtists:
            new_artists = getRelatedArtists(relatedArtistId)
            for newArtist in new_artists:
                depthEdgesList.append((relatedArtistId, newArtist)) #appending tuple to master list
        relatedArtists = new_artists  #relatedArtists repopulated with artists related to first artistID
    for tple in depthEdgesList:
        if tple not in depthEdgesList_checked:
            depthEdgesList_checked.append(tple)
    return depthEdgesList_checked

#print getDepthEdges('43ZHCT0cAZBISjO8DG9PnE', 2)

def getEdgeList(artistID, depth):
    '''Returns list where each edge takes up one row'''
    edgeList = getDepthEdges(artistID, depth)
    return pd.DataFrame(edgeList)

#print getEdgeList('43ZHCT0cAZBISjO8DG9PnE', 2)

def writeEdgeList(artistID, depth, filename):
    edgeList = getEdgeList(artistID, depth)
    edgeList.to_csv(filename, index=False, header=['artist1', 'artist2'])

#writeEdgeList('43ZHCT0cAZBISjO8DG9PnE', 2, 'filename.csv')


    