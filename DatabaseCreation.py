# Refer to Final Project Plan doc for guide

import sqlite3
import os


# Create SQLite Database to store data
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

# Creates 2000 player table with pts, assists, position
def create_2000_all_stars_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS 2000_Info')
    conn.commit()

# Creates 2005 player table with pts, assists, position
def create_2005_all_stars_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS 2005_Info')
    conn.commit()

# Creates 2010 player table with pts, assists, position
def create_2010_all_stars_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS 2010_Info')
    conn.commit()

# Creates 2015 player table with pts, assists, position
def create_2015_all_stars_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS 2015_Info')
    conn.commit()

# Creates 2020 player table with pts, assists, position
def create_2020_all_stars_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS 2020_Info')
    conn.commit()