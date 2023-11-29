# Refer to Final Project Plan doc for guide
# Used for collecting all-star players via Beautiful Soup from https://www.nba.com/news/history-nba-all-star-game

from bs4 import BeautifulSoup
import re
import requests
import unittest
import sqlite3

# Returns list of all all-star players from 2020, 2015, 2010, 2005, 2000 via https://www.nba.com/news/history-nba-all-star-game
def get_all_stars():
    all_stars = []
    years = ['2020', '2015', '2010', '2005', '2000']
    for year in years:
        r = requests.get('https://www.nba.com/news/history-all-star-recap-' + year)
        soup = BeautifulSoup(r.content, 'html.parser')
        container = soup.find('div', class_= 'ArticleContent_article_NBhQ8')
        container.find('h3').find_next('p')


''' Returns dictionary mapping player first and last name to country of origin and last attended
takes in return of get_all_stars'''
def player_background(players):




