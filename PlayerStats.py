# Refer to Final Project Plan doc for guide
# Used to collect players stats, both current and historical from https://www.balldontlie.io/home.html#introduction and to make visualizations

from DatabaseCreation import *
import plotly.graph_objects as go

def avg_assists_by_pos(cur):
    avg_assists_pos_dict = {}
    cur.execute('''SELECT Player_Info.position, AVG(Info_2010.ast) AS average_ast FROM Player_Info JOIN Info_2010 ON Player_Info.id = Info_2010.id 
                    WHERE Player_Info.position = 'G' OR Player_Info.position = 'F' or Player_Info.position = 'C' GROUP BY Player_Info.position''')
    res = cur.fetchall()
    avg_assists_pos_dict['2010'] = dict(res)

    cur.execute('''SELECT Player_Info.position, AVG(Info_2015.ast) AS average_ast FROM Player_Info JOIN Info_2015 ON Player_Info.id = Info_2015.id 
                    WHERE Player_Info.position = 'G' OR Player_Info.position = 'F' or Player_Info.position = 'C' GROUP BY Player_Info.position''')
    res = cur.fetchall()
    avg_assists_pos_dict['2015'] = dict(res)

    cur.execute('''SELECT Player_Info.position, AVG(Info_2020.ast) AS average_ast FROM Player_Info JOIN Info_2020 ON Player_Info.id = Info_2020.id 
                    WHERE Player_Info.position = 'G' OR Player_Info.position = 'F' or Player_Info.position = 'C' GROUP BY Player_Info.position''')
    res = cur.fetchall()
    avg_assists_pos_dict['2020'] = dict(res)

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
    
    title_str = 'Average Number of Assists by Position from 2010, 2015, 2020'
    fig.update_layout(title = title_str, xaxis_tickangle = -45, barmode='group', xaxis = {'tickmode': 'linear'})
    fig.show()

def games_played_across_years(cur):
    cur.execute('SELECT name, games_played FROM Info_2000')
    results_1995 = dict(cur.fetchall())
    games_played_dict = results_1995
    # Sets up dictionary with players as keys and games played from 1995 as values. Values will end up being accumulated games played from all seasons they appeared in.
    
    cur.execute('SELECT name, games_played FROM Info_2000')
    results_2000 = dict(cur.fetchall())
    for res in results_2000:
        if res not in games_played_dict:
            games_played_dict[res] = results_2000[res]
        else:
            games_played_dict[res] += results_2000[res]
    # Adds to dictionary with games played for 2000 all-stars
    
    cur.execute('SELECT name, games_played FROM Info_2005')
    results_2005 = dict(cur.fetchall())
    for res in results_2005:
        if res not in games_played_dict:
            games_played_dict[res] = results_2005[res]
        else:
            games_played_dict[res] += results_2005[res]
    # Adds to dictionary with games played for 2005 all-stars

    cur.execute('SELECT name, games_played FROM Info_2010')
    results_2010 = dict(cur.fetchall())
    for res in results_2010:
        if res not in games_played_dict:
            games_played_dict[res] = results_2010[res]
        else:
            games_played_dict[res] += results_2010[res]
    # Adds to dictionary with games played for 2010 all-stars

    cur.execute('SELECT name, games_played FROM Info_2015')
    results_2015 = dict(cur.fetchall())
    for res in results_2015:
        if res not in games_played_dict:
            games_played_dict[res] = results_2015[res]
        else:
            games_played_dict[res] += results_2015[res]
    # Adds to dictionary with games played for 2015 all-stars

    cur.execute('SELECT name, games_played FROM Info_2020')
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

    games_played_1995 = [results_1995[names[0]], results_1995[names[1]], results_1995[names[2]], results_1995[names[3]], results_1995[names[4]]]
    games_played_2000 = [results_2000[names[0]], results_2000[names[1]], results_2000[names[2]], results_2000[names[3]], results_2000[names[4]]]
    games_played_2005 = [results_2005[names[0]], results_2005[names[1]], results_2005[names[2]], results_2005[names[3]], results_2005[names[4]]]
    games_played_2010 = [results_2010[names[0]], results_2010[names[1]], results_2010[names[2]], results_2010[names[3]], results_2010[names[4]]]
    games_played_2015 = [results_2015[names[0]], results_2015[names[1]], results_2015[names[2]], results_2015[names[3]], results_2015[names[4]]]
    games_played_2020 = [results_2020[names[0]], results_2020[names[1]], results_2020[names[2]], results_2020[names[3]], results_2020[names[4]]]

    plot = go.Figure(data=[go.Bar(
        name = '1995 games played',
        x = names,
        y = games_played_1995
    ),
    go.Bar(
        name = '2000 games played',
        x = names,
        y = games_played_2000
    ), 
    go.Bar(
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
    
def games_played_across_years2(cur):
   # Fetch games played and player id for each year
    years = ['1995', '2000', '2005', '2010', '2015', '2020']

    # Initialize a dictionary to store total games played for each player and each year
    games_played_dict = {}

    for year in years:
        cur.execute(f"SELECT id, games_played FROM Info_{year}")
        year_results = dict(cur.fetchall())

        # Process games played results for each year
        for player_id, games_played in year_results.items():
            if player_id not in games_played_dict:
                games_played_dict[player_id] = {year: games_played}
            else:
                games_played_dict[player_id][year] = games_played_dict[player_id].get(year, 0) + games_played

    # Fetch player names corresponding to player ids
    player_names = {}
    cur.execute('SELECT id, name FROM Player_Info')
    player_info_results = dict(cur.fetchall())
    for player_id in games_played_dict.keys():
        if player_id in player_info_results:
            player_names[player_id] = player_info_results[player_id]

    # Sort players by total games played
    sort_games_played = sorted(games_played_dict.items(), key=lambda t: sum(t[1].values()), reverse=True)

    # Get top 5 player names and total games played
    top_players = sort_games_played[:5]
    player_ids, total_games_played = zip(*top_players)
    player_names_top5 = [player_names[player_id] for player_id in player_ids]

    # Create and show the plot
    plot = go.Figure(data=[go.Bar(
        name=f'{year} games played',
        x=player_names_top5,
        y=[games_played_dict[player_id].get(year, 0) for player_id in player_ids]
    ) for year in years])

    plot.update_layout(barmode='stack', title='Top 5 Players by Total Games Played Across Years')
    plot.show()
    
def top_players_by_total_pts_and_ast_with_games_played(cur):
    # Fetch total points, total assists, and total games played for each player across years
    cur.execute("""
        SELECT p.id, 
               SUM(i.pts * i.games_played) as total_pts, 
               SUM(i.ast * i.games_played) as total_ast,
               SUM(i.games_played) as total_games_played
        FROM (
            SELECT id, pts, ast, games_played FROM Info_1995
            UNION ALL
            SELECT id, pts, ast, games_played FROM Info_2000
            UNION ALL
            SELECT id, pts, ast, games_played FROM Info_2005
            UNION ALL
            SELECT id, pts, ast, games_played FROM Info_2010
            UNION ALL
            SELECT id, pts, ast, games_played FROM Info_2015
            UNION ALL
            SELECT id, pts, ast, games_played FROM Info_2020
        ) AS i
        JOIN Player_Info AS p ON i.id = p.id
        GROUP BY p.id
    """)
    total_results = cur.fetchall()

    # Fetch player names corresponding to player ids
    player_names = {}
    cur.execute('SELECT id, name FROM Player_Info')
    player_info_results = dict(cur.fetchall())
    for player_id, player_name in player_info_results.items():
        player_names[player_id] = player_name

    # Calculate the total points, total assists, and total games played for each player
    total_pts_dict = {}
    total_ast_dict = {}
    total_games_played_dict = {}
    for player_id, total_pts, total_ast, total_games_played in total_results:
        total_pts_dict[player_id] = total_pts
        total_ast_dict[player_id] = total_ast
        total_games_played_dict[player_id] = total_games_played

    # Sort players by the sum of total points and total assists multiplied by total games played
    sort_total_sum = sorted(total_pts_dict.items(), key=lambda t: (total_pts_dict[t[0]] + total_ast_dict[t[0]]) * total_games_played_dict[t[0]], reverse=True)

    # Get top 5 player names and total sums
    top_players = sort_total_sum[:5]
    player_ids, total_sums = zip(*top_players)
    player_names_top5 = [player_names.get(player_id, f"Unknown Player {player_id}") for player_id in player_ids]

    # Create and show the combined bar plot for total points and total assists
    plot_combined = go.Figure()

    plot_combined.add_trace(go.Bar(
        name='Total PTS',
        x=player_names_top5,
        y=[total_pts_dict[player_id] for player_id in player_ids],
        offsetgroup=0
    ))

    plot_combined.add_trace(go.Bar(
        name='Total AST',
        x=player_names_top5,
        y=[total_ast_dict[player_id] for player_id in player_ids],
        offsetgroup=1
    ))

    plot_combined.update_layout(title='Top 5 Players by Total PTS and AST Across Years', barmode='stack')
    plot_combined.show()
    
def total_pts_and_ast_comparison(cur):
    # Fetch total points and total assists for all players across years
    cur.execute("""
        SELECT
            year,
            SUM(pts * games_played) as total_pts,
            SUM(ast * games_played) as total_ast
        FROM (
            SELECT '1995' as year, pts, ast, games_played FROM Info_1995
            UNION ALL
            SELECT '2000' as year, pts, ast, games_played FROM Info_2000
            UNION ALL
            SELECT '2005' as year, pts, ast, games_played FROM Info_2005
            UNION ALL
            SELECT '2010' as year, pts, ast, games_played FROM Info_2010
            UNION ALL
            SELECT '2015' as year, pts, ast, games_played FROM Info_2015
            UNION ALL
            SELECT '2020' as year, pts, ast, games_played FROM Info_2020
        )
        GROUP BY year
    """)
    total_results = cur.fetchall()

    # Extract years, total points, and total assists
    years, total_pts, total_ast = zip(*total_results)

    # Create a stacked bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(x=years, y=total_pts, name='Total Points', marker_color='blue'))
    fig.add_trace(go.Bar(x=years, y=total_ast, name='Total Assists', marker_color='orange'))

    fig.update_layout(barmode='stack', title='Comparison of Total Points and Total Assists Across Years')
    fig.show()

    


def main():
    # Sets up connection to the database
    cur, conn = set_up_database('NBA All-Star Info')
    
    
    
    # Used to make assist by position visualization for three years of data (2010, 2015, 2020)
    years_for_ast_vis = ['2010', '2015', '2020']
    avg_ast_pos_dict = avg_assists_by_pos(cur)
    make_avg_assists_vis(avg_ast_pos_dict, years_for_ast_vis)
    
    
    # Used to make top 5 playes by games played plot - stacked with amount of games played in each year [1995, 2000, 2005, 2010, 2015, 2020]
    games_played_across_years2(cur)
    
    top_players_by_total_pts_and_ast_with_games_played(cur)
    
    total_pts_and_ast_comparison(cur)
    

    
    

if __name__ == '__main__':
    main()