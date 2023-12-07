import sqlite3
import os
from DatabaseCreation import *

def main():
    years = [1995, 2000, 2005, 2010, 2015, 2020]

    cur, conn = set_up_database('NBA All-Star Info')
    create_player_lookup_table(cur, conn)

    all_stars_by_year = get_all_stars(years)
    player_id_dict, player_position_dict, ids_by_year = id_pos_for_player(all_stars_by_year)

    # NEED TO BALANCE THE FUNCTION BELOW SO THAT IT ONLY INSERTS 25 at a time
    insert_player_lookup_table(cur, conn, player_id_dict, player_position_dict)

    conn.close()

if __name__ == '__main__':
    main()