import sqlite3
import os


# Create SQLite Database to store data
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

# Creates 2010 player table with pts, assists, rebounds, position
def create_2010_player_table(cur):
    cur.execute('CREATE TABLE IF NOT EXISTS 2010_Info')

# Creates 2015 player table with pts, assists, rebounds, position
def create_2015_player_table(cur):
    cur.execute('CREATE TABLE IF NOT EXISTS 2015_Info')

# Creates 2020 player table with pts, assists, rebounds, position
def create_2020_player_table(cur):
    cur.execute('CREATE TABLE IF NOT EXISTS 2020_Info')