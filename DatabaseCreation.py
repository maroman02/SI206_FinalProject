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
    cur.execute('CREATE TABLE IF NOT EXISTS 2000_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC games_played NUMERIC)')

    # Creates 2005 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2005_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC games_played NUMERIC)')

    # Creates 2010 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2010_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC games_played NUMERIC)')

    # Creates 2015 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2015_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC games_played NUMERIC)')

    # Creates 2020 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS 2020_Info (id INTEGER PRIMARY KEY name TEXT position TEXT pts NUMERIC ast NUMERIC games_played NUMERIC)')
    
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

def position_for_player(player_id_dict):
    player_position_dict = {}
    for player in player_id_dict:
        r = requests.get('https://www.balldontlie.io/api/v1/players/' + str(player_id_dict[player]))
        player_data = r.json()
        position = player_data['data'][0]['position']
        player_position_dict[player] = position

    return player_position_dict

def get_player_stats(year_dict, player_id_dict):
    player_stats_by_year = {}
    for year in year_dict:
        dict_of_player_stats = {}
        for player in year:
            params = {'season': year, 'player_ids': [player_id_dict[player]]}
            r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
            raw_data = r.json()
            pts = float(raw_data['data'][0]['pts'])
            ast = float(raw_data['data'][0]['ast'])
            games_played = int(raw_data['data'][0]['games_played'])
            player_stats = [pts, ast, games_played]
            dict_of_player_stats[player] = player_stats
        player_stats_by_year[year] = dict_of_player_stats


def insertData(cur, conn, player_stats_by_year, player_id_dict, player_position_dict):
    for year in player_stats_by_year:
        for player in year:
            insertion_tuple = (str(year) + '_Info', player_id_dict[player], player, player_position_dict[player], player_stats_by_year[year][player][0], player_stats_by_year[year][player][1], player_stats_by_year[year][player][2])
            cur.execute('INSERT OR IGNORE INTO ? (id, name, position, pts, ast, games_played) VALUES (?, ?, ?, ?, ?, ?, ?)', (insertion_tuple))

    conn.commit()
