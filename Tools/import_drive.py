import os
import json

BASE = "KEITTOKIRJA"
WORD = "Reseptit"
JSON = "Json"
IMGS = "Reseptien kuvat"


def parseJSON(file):
    file_path = os.path.join(BASE, JSON, file)
    with open(file_path, 'r', encoding="utf-8") as f:
        data = json.load(f)
        
    for food in data['foods']:
        print('Name: '+food['name'])
        for ing in food['ings']:
            print('Sub ingredient: '+ing['name'])
            print(ing['ings'].split('|'))
            
        print('Steps: ')
        print(food['steps'].split('|'))
        print('Hints: ')
        print(food['hints'].split('|'))
'''
text_entries = os.listdir(os.path.join(BASE, JSON))

for text in text_entries:
    parseJSON(text)'''
    
    
with open(os.path.join(BASE, JSON, "BBQ-kanapizza.json"), 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(json.dumps(data['foods'][0]['ings']))