# Refer to Final Project Plan doc for guide

import sqlite3
import os
from PlayerLookup import *
import time


# Create SQLite Database to store data
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

# Create player lookup table
def create_player_lookup_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS Player_Info (id INTEGER PRIMARY KEY, name TEXT, position TEXT)')
    conn.commit()

def insert_player_lookup_table(cur, conn, player_id_dict, player_position_dict, batch_size=25):
    cur.execute('SELECT MAX(id) FROM Player_Info')
    last_inserted_id = cur.fetchone()[0] or 0

    player_list = [(player, player_id_dict[player], player_position_dict[player]) for player in player_id_dict if player_id_dict[player] > last_inserted_id]
    player_list.sort(key=lambda x: x[1])

    for i in range(0, min(batch_size, len(player_list))):
        player, player_id, position = player_list[i]
        cur.execute('INSERT OR IGNORE INTO Player_Info (id, name, position) VALUES (?, ?, ?)', (player_id, player, position))

    conn.commit()

# Creates tables with all-star player stats from each year in [1995, 2000, 2005, 2010, 2015, 2020]
def create_stats_tables(cur, conn):
    # Creates 1995 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS Info_1995 (id INTEGER, pts NUMERIC, ast NUMERIC, games_played INTEGER)')

    # Creates 2000 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS Info_2000 (id INTEGER, pts NUMERIC, ast NUMERIC, games_played INTEGER)')

    # Creates 2005 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS Info_2005 (id INTEGER, pts NUMERIC, ast NUMERIC, games_played INTEGER)')

    # Creates 2010 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS Info_2010 (id INTEGER, pts NUMERIC, ast NUMERIC, games_played INTEGER)')

    # Creates 2015 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS Info_2015 (id INTEGER, pts NUMERIC, ast NUMERIC, games_played INTEGER)')

    # Creates 2020 player table with pts, assists, position
    cur.execute('CREATE TABLE IF NOT EXISTS Info_2020 (id INTEGER, pts NUMERIC, ast NUMERIC, games_played INTEGER)')
    
    conn.commit()

def id_pos_for_player(all_stars_by_year):
    player_id_dict = {}
    ids_by_year = {}
    player_position_dict = {}
    for year in all_stars_by_year:
        ids = []
        for player in all_stars_by_year[year]:
            if player in player_id_dict:
                ids.append(player_id_dict[player])
                continue
            if player == 'Manu Ginóbili':
                player = 'Manu Ginobili'
            elif player == 'Luka Dončić':
                player = 'Luka Doncic'
            elif player == 'Nikola Jokić':
                player = 'Nikola Jokic'
            r = requests.get('https://www.balldontlie.io/api/v1/players', params={'search': player})
            player_data = r.json()
            id = int(player_data['data'][0]['id'])
            ids.append(id)

            position_raw = player_data['data'][0]['position']
            if position_raw != '':
                position = position_raw[0]
            else:
                position = position_raw
            player_id_dict[player] = id
            player_position_dict[player] = position

            time.sleep(0.8)

        ids_by_year[year] = ids

    return player_id_dict, player_position_dict, ids_by_year

def get_player_stats_1995(ids_by_year):
    dict_of_player_stats = {}
    params = {'season': 1995, 'player_ids[]': ids_by_year[1995]}
    r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    raw_data = r.json()
    for player in raw_data['data']:
        pts = float(player['pts'])
        ast = float(player['ast'])
        games_played = int(player['games_played'])
        player_stats = [pts, ast, games_played]
        dict_of_player_stats[player['player_id']] = player_stats

    return dict_of_player_stats


def get_player_stats_2000(ids_by_year):
    dict_of_player_stats = {}
    params = {'season': 2000, 'player_ids[]': ids_by_year[2000]}
    r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    raw_data = r.json()
    for player in raw_data['data']:
        pts = float(player['pts'])
        ast = float(player['ast'])
        games_played = int(player['games_played'])
        player_stats = [pts, ast, games_played]
        dict_of_player_stats[player['player_id']] = player_stats

    return dict_of_player_stats

def get_player_stats_2005(ids_by_year):
    dict_of_player_stats = {}
    params = {'season': 2005, 'player_ids[]': ids_by_year[2005]}
    r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    raw_data = r.json()
    for player in raw_data['data']:
        pts = float(player['pts'])
        ast = float(player['ast'])
        games_played = int(player['games_played'])
        player_stats = [pts, ast, games_played]
        dict_of_player_stats[player['player_id']] = player_stats

    return dict_of_player_stats

def get_player_stats_2010(ids_by_year):
    dict_of_player_stats = {}
    params = {'season': 2010, 'player_ids[]': ids_by_year[2010]}
    r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    raw_data = r.json()
    for player in raw_data['data']:
        pts = float(player['pts'])
        ast = float(player['ast'])
        games_played = int(player['games_played'])
        player_stats = [pts, ast, games_played]
        dict_of_player_stats[player['player_id']] = player_stats

    return dict_of_player_stats

def get_player_stats_2015(ids_by_year):
    dict_of_player_stats = {}
    params = {'season': 2015, 'player_ids[]': ids_by_year[2015]}
    r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    raw_data = r.json()
    for player in raw_data['data']:
        pts = float(player['pts'])
        ast = float(player['ast'])
        games_played = int(player['games_played'])
        player_stats = [pts, ast, games_played]
        dict_of_player_stats[player['player_id']] = player_stats

    return dict_of_player_stats

def get_player_stats_2020(ids_by_year):
    dict_of_player_stats = {}
    params = {'season': 2020, 'player_ids[]': ids_by_year[2020]}
    r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params)
    raw_data = r.json()
    for player in raw_data['data']:
        pts = float(player['pts'])
        ast = float(player['ast'])
        games_played = int(player['games_played'])
        player_stats = [pts, ast, games_played]
        dict_of_player_stats[player['player_id']] = player_stats

    return dict_of_player_stats


def insertData_1995(cur, conn, dict_of_player_stats):
    for id in dict_of_player_stats:
        insertion_tuple = (id, dict_of_player_stats[id][0], dict_of_player_stats[id][1], dict_of_player_stats[id][2])
        cur.execute('INSERT OR IGNORE INTO Info_1995 (id, pts, ast, games_played) VALUES (?, ?, ?, ?)', (insertion_tuple))

    conn.commit()

def insertData_2000(cur, conn, dict_of_player_stats):
    for id in dict_of_player_stats:
        insertion_tuple = (id, dict_of_player_stats[id][0], dict_of_player_stats[id][1], dict_of_player_stats[id][2])
        cur.execute('INSERT OR IGNORE INTO Info_2000 (id, pts, ast, games_played) VALUES (?, ?, ?, ?)', (insertion_tuple))

    conn.commit()

def insertData_2005(cur, conn, dict_of_player_stats):
    for id in dict_of_player_stats:
        insertion_tuple = (id, dict_of_player_stats[id][0], dict_of_player_stats[id][1], dict_of_player_stats[id][2])
        cur.execute('INSERT OR IGNORE INTO Info_2005 (id, pts, ast, games_played) VALUES (?, ?, ?, ?)', (insertion_tuple))

    conn.commit()

def insertData_2010(cur, conn, dict_of_player_stats):
    for id in dict_of_player_stats:
        insertion_tuple = (id, dict_of_player_stats[id][0], dict_of_player_stats[id][1], dict_of_player_stats[id][2])
        cur.execute('INSERT OR IGNORE INTO Info_2010 (id, pts, ast, games_played) VALUES (?, ?, ?, ?)', (insertion_tuple))

    conn.commit()

def insertData_2015(cur, conn, dict_of_player_stats):
    for id in dict_of_player_stats:
        insertion_tuple = (id, dict_of_player_stats[id][0], dict_of_player_stats[id][1], dict_of_player_stats[id][2])
        cur.execute('INSERT OR IGNORE INTO Info_2015 (id, pts, ast, games_played) VALUES (?, ?, ?, ?)', (insertion_tuple))

    conn.commit()

def insertData_2020(cur, conn, dict_of_player_stats):
    for id in dict_of_player_stats:
        insertion_tuple = (id, dict_of_player_stats[id][0], dict_of_player_stats[id][1], dict_of_player_stats[id][2])
        cur.execute('INSERT OR IGNORE INTO Info_2020 (id, pts, ast, games_played) VALUES (?, ?, ?, ?)', (insertion_tuple))

    conn.commit()


def main():
    pass

if __name__ == '__main__':
    main()