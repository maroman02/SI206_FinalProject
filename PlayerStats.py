# Used to collect players stats, both current and historical from https://www.balldontlie.io/home.html#introduction

import unittest
import sqlite3
import requests
import json
import os


# Create SQLite Database to store data
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

# Creates 2010 player table with pts, assists, rebounds, position
def create_2010_player_table(cur):
    cur.execute('CREATE')

# Creates 2015 player table with pts, assists, rebounds, position
def create_2015_player_table(cur):
    cur.execute('CREATE')

# Creates 2020 player table with pts, assists, rebounds, position
def create_2020_player_table(cur):
    cur.execute('CREATE')

# Returns data from API
def get_json_obj(url, params):
    try: 
        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()
    
    except:
        print('Exception!')
        return None
    


    

    
