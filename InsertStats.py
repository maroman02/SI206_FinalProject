from DatabaseCreation import *
import time

def main():
    years = [1995, 2000, 2005, 2010, 2015, 2020]
    cur, conn = set_up_database('NBA All-Star Info')
    create_stats_tables(cur, conn)

    all_stars_by_year = get_all_stars(years)
    player_id_dict, player_position_dict, ids_by_year = id_pos_for_player(all_stars_by_year)
    
    dict_of_player_stats_1995 = get_player_stats_1995(ids_by_year)
    dict_of_player_stats_2000 = get_player_stats_2000(ids_by_year)
    time.sleep(2)
    dict_of_player_stats_2005 = get_player_stats_2005(ids_by_year)
    dict_of_player_stats_2010 = get_player_stats_2010(ids_by_year)
    dict_of_player_stats_2015 = get_player_stats_2015(ids_by_year)
    dict_of_player_stats_2020 = get_player_stats_2020(ids_by_year)

    insertData_1995(cur, conn, dict_of_player_stats_1995)
    insertData_2000(cur, conn, dict_of_player_stats_2000)
    insertData_2005(cur, conn, dict_of_player_stats_2005)
    insertData_2010(cur, conn, dict_of_player_stats_2010)
    insertData_2015(cur, conn, dict_of_player_stats_2015)
    insertData_2020(cur, conn, dict_of_player_stats_2020)

    conn.close()

if __name__ == '__main__':
    main()
