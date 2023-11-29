# Used to collect players stats, both current and historical from https://www.balldontlie.io/home.html#introduction

import unittest
import requests
import json
import os


# Returns data from API
def get_json_obj(url, params):
    try: 
        r = requests.get(url, params)
        r.raise_for_status()
        return r.json()
    
    except:
        print('Exception!')
        return None
    

    


    

    
