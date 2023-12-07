# Refer to Final Project Plan doc for guide
# Used for collecting all-star players via Beautiful Soup from Basketball Reference
from bs4 import BeautifulSoup
import re
import requests
import unittest

# Returns dictionary with key year and value list of all all-star players. Years considered are 2020, 2015, 2010, 2005, 2000, 1995 via Basketball Reference
def get_all_stars(years):
    all_stars_by_year = {}
    for year in years:
        all_stars = []
        r = requests.get('https://www.basketball-reference.com/allstar/NBA_' + str(year) + '.html')
        soup = BeautifulSoup(r.content, 'html.parser')
        container = soup.find_all('table', class_= "sortable stats_table")
        for table in container:
            players = table.find_all('th', {'scope': 'row'})
            for player in players:
                if player.find('a') != None:
                    name = player.find('a').text
                all_stars.append(name)
        all_stars_by_year[year] = all_stars

    return all_stars_by_year


def main():
    years = [1995, 2000, 2005, 2010, 2015, 2020]
    get_all_stars


if __name__ == '__main__':
    main()




