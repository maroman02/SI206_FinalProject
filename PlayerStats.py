# Refer to Final Project Plan doc for guide
# Used to collect players stats, both current and historical from https://www.balldontlie.io/home.html#introduction and to make visualizations

import unittest
import requests
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

def ppg_for_players_in_2015_and_2020(cur):
    cur.execute('''SELECT 2020_Info.name, ((2020_Info.ppg + 2015_Info.ppg) / 2) AS ppg_average FROM 2020_Info 
                JOIN 2015_Info ON 2020_Info.name = 2015_Info.name SORT BY ppg_average DESC LIMIT 5''')
    res = cur.fetchall()
    names, ppg_avg = zip(*res)
    fig = go.Figure(
        data = [go.Bar(x = names, y = ppg_avg)],
        layout = dict(title = dict(text = 'Top 5 Players Appearing in Both 2015 and 2020 All-Star Game by PPG'))
    )
    fig.show()


def games_played_across_years(cur, years):
    cur.execute('SELECT name, games_played FROM 2000_Info')
    results_2000 = dict(cur.fetchall())
    games_played_dict = results_2000
    # Sets up dictionary with players as keys and games played from 2000 as values. Values will end up being accumulated games played from all seasons they appeared in.
    
    cur.execute('SELECT name, games_played FROM 2005_Info')
    results_2005 = dict(cur.fetchall())
    for res in results_2005:
        if res not in games_played_dict:
            games_played_dict[res] = results_2005[res]
        else:
            games_played_dict[res] += results_2005[res]
    # Adds to dictionary with games played for 2005 all-stars

    cur.execute('SELECT name, games_played FROM 2010_Info')
    results_2010 = dict(cur.fetchall())
    for res in results_2010:
        if res not in games_played_dict:
            games_played_dict[res] = results_2010[res]
        else:
            games_played_dict[res] += results_2010[res]
    # Adds to dictionary with games played for 2010 all-stars

    cur.execute('SELECT name, games_played FROM 2015_Info')
    results_2015 = dict(cur.fetchall())
    for res in results_2015:
        if res not in games_played_dict:
            games_played_dict[res] = results_2015[res]
        else:
            games_played_dict[res] += results_2015[res]
    # Adds to dictionary with games played for 2015 all-stars

    cur.execute('SELECT name, games_played FROM 2020_Info')
    results_2020 = dict(cur.fetchall())
    for res in results_2020:
        if res not in games_played_dict:
            games_played_dict[res] = results_2020[res]
        else:
            games_played_dict[res] += results_2020[res]
    # Adds to dictionary with games played for 2020 all-stars

    sort_games_played = sorted(games_played_dict.items(), key=lambda t:t[0], reverse=True)

    names, total_games_played = zip(*sort_games_played)

    names = names[:5]

    games_played_2000 = [results_2000[names[0]], results_2000[names[1]], results_2000[names[2]], results_2000[names[3]], results_2000[names[4]]]
    games_played_2005 = [results_2005[names[0]], results_2005[names[1]], results_2005[names[2]], results_2005[names[3]], results_2005[names[4]]]
    games_played_2010 = [results_2010[names[0]], results_2010[names[1]], results_2010[names[2]], results_2010[names[3]], results_2010[names[4]]]
    games_played_2015 = [results_2015[names[0]], results_2015[names[1]], results_2015[names[2]], results_2015[names[3]], results_2015[names[4]]]
    games_played_2020 = [results_2020[names[0]], results_2020[names[1]], results_2020[names[2]], results_2020[names[3]], results_2020[names[4]]]

    plot = go.Figure(data=[go.Bar(
        name = '2000 games played',
        x = names,
        y = games_played_2000
    ), go.Bar(
        name = '2005 games played',
        x = names,
        y = games_played_2005
    ),
        go.Bar(
        name = '2010 games played',
        x = names,
        y = games_played_2010
    ),
        go.Bar(
        name = '2015 games played',
        x = names,
        y = games_played_2015
    ),
        go.Bar(
        name = '2020 games played',
        x = names,
        y = games_played_2020
    )])

    plot.update_layout(barmode='stack')
    plot.show()