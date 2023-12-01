# Refer to Final Project Plan doc for guide
# Used to collect players stats, both current and historical from https://www.balldontlie.io/home.html#introduction and to make visualizations

import unittest
import requests
import json
import os
from DatabaseCreation import *
import plotly.graph_objects as go

def avg_assists_by_pos(cur, years):
    avg_assists_pos_dict = {}
    for year in years:
        cur.execute('''SELECT position, AVG(ast) AS average_ast FROM ? 
                    WHERE position = G OR position = F or position = C GROUP BY position''', (str(year) + '_Info'))
        res = cur.fetchall()
        avg_assists_pos_dict[year] = dict(res)

    return avg_assists_pos_dict

def make_avg_assists_vis(avg_assists_pos_dict, years):
    G_assists_by_year = []
    F_assists_by_year = []
    C_assists_by_year = []
    for year in avg_assists_pos_dict:
        G_assists_by_year.append(avg_assists_pos_dict[year]['G'])
        F_assists_by_year.append(avg_assists_pos_dict[year]['F'])
        C_assists_by_year.append(avg_assists_pos_dict[year]['C'])
    
    fig = go.Figure(data = [
        go.Bar(name = 'G', x = years, y = G_assists_by_year),
        go.Bar(name = 'F', x = years, y = F_assists_by_year),
        go.Bar(name = 'C', x = years, y = C_assists_by_year)
        ])
    title_str = 'Average Number of Assists by Position from 2000, 2005, 2010, 2015, 2020'
    fig.update_layout(title = title_str, xaxis_tickangle = -45, barmode='group', xaxis = {'tickmode': 'linear'})
    fig.show()

def games_played_2020(cur):
    cur.execute('SELECT name, games_played From 2020_Info SORT BY games_played DESC LIMIT 10')
    res = cur.fetchall()
    x,y = zip(*res)



def highest_ppg(cur, years):
    pass