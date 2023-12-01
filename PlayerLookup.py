# Refer to Final Project Plan doc for guide
# Used for collecting all-star players via Beautiful Soup from https://www.landofbasketball.com/allstargames/year_by_year_results.htm

from bs4 import BeautifulSoup
import re
import requests
import unittest
import sqlite3

# Returns dictionary with key year and value list of all all-star players. Years considered are 2020, 2015, 2010, 2005, 2000 via https://www.landofbasketball.com/allstargames/year_by_year_results.htm
def get_all_stars(years):
    all_stars_by_year = {}
    for year in years:
        all_stars = []
        r = requests.get('https://www.landofbasketball.com/allstargames/' + str(year) + '_nba_all_star_game.htm')
        soup = BeautifulSoup(r.content, 'html.parser')
        container = soup.find_all('tr', class_= 'a-top')
        for player in container:
            name = player.find('a').text
            all_stars.append(name)
        all_stars_by_year[year] = all_stars







