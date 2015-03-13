from flask import Flask, render_template, request, redirect, url_for
import pymysql
import networkx as nx
import pandas as pd
import random
from io import open
import json
from pprint import pprint



dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

app = Flask(__name__)

def createAttributesTable(json_file):
    
    json_data = open(json_file)
    data = json.load(json_data)

    friend_attribute_list = []
    for friend in data:       # friend indicates one dictionary
        uid = friend["uid"]
        first_name = friend["first_name"]
        middle_name = friend["middle_name"]
        last_name = friend["last_name"]
        pic = friend["pic"]
        religion = friend["religion"]
        birthday_date = friend["birthday_date"]
        sex = friend["sex"]
        hometown_location = friend["hometown_location"]
        current_location = friend["current_location"]
        relationship_status = friend["relationship_status"]
        significant_other_id = friend["significant_other_id"]
        political = friend["political"]
        locale = friend["locale"]
        profile_url = friend["profile_url"]
        website = friend["website"]

        tupl = (uid, first_name, middle_name, last_name, pic, religion, birthday_date, sex, hometown_location, current_location, relationship_status, significant_other_id, political, locale, profile_url, website)
        friend_attribute_list.append(tupl)

    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS friend_attributes (id INTEGER PRIMARY KEY AUTO_INCREMENT, uid INTEGER, first_name VARCHAR(128), middle_name VARCHAR(128), last_name VARCHAR(128), pic VARCHAR(255), religion VARCHAR(128), birthday_date INTEGER, sex VARCHAR(64), hometown_location VARCHAR(128), current_location VARCHAR(128), relationship_status VARCHAR(64), significant_other_id INTEGER, political VARCHAR(128), locale VARCHAR(64), profile_url VARCHAR(255), website VARCHAR(128));''')

    insertQuery = '''INSERT INTO friend_attributes (uid, first_name, middle_name, last_name, pic, religion, birthday_date, sex, hometown_location, current_location, relationship_status, significant_other_id, political, locale, profile_url, website) \n
                         VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)'''

    cur.executemany(insertQuery, friend_attribute_list)
    db.commit()

createAttributesTable('friend_attributes.json')



