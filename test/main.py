# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    
    try:
        with open('json-joker.json', 'w') as dataFile:
            json.dump(r.json(), dataFile, indent=4)
        print("Se escribe en el archivo sin problemas")
        return 0
    except:
        print("Error al escribir en el archivo")
        return 1
    
