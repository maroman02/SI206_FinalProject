# Refer to Final Project Plan doc for guide

import sqlite3
import os
from PlayerLookup import *


# Create SQLite Database to store data
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

# Creates tables with all-star player stats from each year in [2000, 2005, 2010, 2015, 2020]
def create_all_stars_tables(cur, conn):
    # Creates 2000 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2000_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC)')

    # Creates 2005 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2005_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC)')

    # Creates 2010 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2010_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC)')

    # Creates 2015 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2015_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC)')

    # Creates 2020 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2020_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC)')
    
    conn.commit()

def id_for_player(year_dict):
    player_id_dict = {}
    for year in year_dict:
        for player in year:
            r = requests.get('https://www.balldontlie.io/api/v1/players', params={'search': player})
            player_data = r.json()
            id = int(player_data['data'][0]['id'])
            player_id_dict[player] = id

    return player_id_dict

def get_player_stats(year_dict, player_id_dict):
    player_stats_by_year = {}
    for year in year_dict:
        for player in year:
            params = {'season': year, 'player_ids': [player_id_dict[player]]}
            r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    

def insertData(cur, conn, year_dict):
    pass
