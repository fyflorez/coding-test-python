# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests
from colorama import Back, init

init()

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    
    try:
        with open('json-joker.json', 'w') as dataFile:
            json.dump(r.json(), dataFile, indent=4)
        
        text = json.dumps(r.json())
        
        print(Back.BLUE + "Json \n" + text)

        with open('joker.txt', 'w') as dataFile:
            json.dump(r.json()["value"], dataFile, indent=4)  
    
        return 0
    except:
        return 1
    
