import unittest
from DatabaseCreation import *
from PlayerLookup import *
from PlayerStats import *

def main():
    years = [1995, 2000, 2005, 2010, 2015, 2020]
    cur, conn = set_up_database('NBA All-Star Info')
    create_stats_tables(cur, conn)

    all_stars_by_year = get_all_stars(years)
    player_id_dict, player_position_dict, ids_by_year = id_pos_for_player(all_stars_by_year)
