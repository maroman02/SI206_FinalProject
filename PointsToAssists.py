
import unittest
import requests
import os
from DatabaseCreation import *
import plotly.graph_objects as go

def calculate_pts_to_ast_ratio(cur):
    # Fetch player points and assists for all years
    cur.execute('''SELECT id, pts, ast FROM Info_1995
                   UNION ALL
                   SELECT id, pts, ast FROM Info_2000
                   UNION ALL
                   SELECT id, pts, ast FROM Info_2005
                   UNION ALL
                   SELECT id, pts, ast FROM Info_2010
                   UNION ALL
                   SELECT id, pts, ast FROM Info_2015
                   UNION ALL
                   SELECT id, pts, ast FROM Info_2020''')
    results = cur.fetchall()

    # Calculate the ratio of points to assists for each player
    pts_to_ast_ratio = {}
    for player_id, points, assists in results:
        if assists != 0:
            pts_to_ast_ratio[player_id] = points / assists

    return pts_to_ast_ratio

def save_pts_to_ast_ratio_to_file(pts_to_ast_ratio, player_names, output_file):
    with open(output_file, 'w') as file:
        file.write("Player\tPoints to Assists Ratio\n")
        for player_id, ratio in pts_to_ast_ratio.items():
            player_name = player_names.get(player_id, f'Player_{player_id}')
            file.write(f"{player_name}\t{ratio:.2f}\n")

def do_pts_to_ast_ratio():
    # Sets up connection to the database
    cur, conn = set_up_database('NBA All-Star Info')

    # Fetch player names corresponding to player ids
    player_names = {}
    cur.execute('SELECT id, name FROM Player_Info')
    player_info_results = dict(cur.fetchall())
    for player_id in player_info_results.keys():
        player_names[player_id] = player_info_results[player_id]

    # Calculate points to assists ratio
    pts_to_ast_ratio = calculate_pts_to_ast_ratio(cur)

    # Specify the output file
    output_file = 'points_to_assists_ratio.txt'

    # Save the results to a text file
    save_pts_to_ast_ratio_to_file(pts_to_ast_ratio, player_names, output_file)

def main():
    do_pts_to_ast_ratio()
    
if __name__ == '__main__':
    main()