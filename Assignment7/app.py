from flask import Flask, render_template, request, redirect, url_for
import pymysql
import networkx as nx
import pandas as pd
import random
from io import open
from fetchArtist import *
from fetch Albums import *
from artistNetworks import getEdgeList
from analyzeNetworks import randomCentralNode, pandasToNetworkX


dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

app = Flask(__name__)

def createNewPlaylist(artist_name):
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(128));''')
    cur.execute('''CREATE TABLE IF NOT EXISTS songs (playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(128), albumName VARCHAR(256));''')

    artists_id = fetchArtistId(artist_name)
    edge_list = getEdgeList(artists_id, 2)
    g = pandasToNetworkX(edge_list)

    randomArtists=[]

    limit = 30
    while limit > 0:
        random_artist = randomCentralNode(G)
        album_id_list = fetchAlbumIds(random_artist)
        if album_id_list == []:
            pass
        else:
            randomArtists.append(random_artist)
            limit -= 1


@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        # YOUR CODE HERE
        return(redirect("/playlists/"))



if __name__ == '__main__':
    app.debug=True
    app.run()