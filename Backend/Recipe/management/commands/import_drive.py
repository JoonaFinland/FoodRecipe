from django.core.management.base import BaseCommand, CommandError
from Recipe.models import Recipe, Food
from django.core.files import File

import os
import json

BASE = "B:\\Python\\FoodRecipe\\Tools\\KEITTOKIRJA"
WORD = "Reseptit"
JSON = "Json"
IMGS = "Reseptien kuvat"


def convert_dict(dict):
    out = []
    for key,val in dict.items():
        out.append({
            'name': key.rstrip(),
            'ings': '|'.join(val)
        })
    return json.dumps(out)

def parseJSON(file):
    file_path = os.path.join(BASE, JSON, file)
    image_path = os.path.join(BASE, IMGS, file.split('.')[0]+'.jpg')
    with open(file_path, 'r', encoding="utf-8") as f:
        data = json.load(f)
        
    recipe_name = file.split('.')[0]
    recipe_img = open(image_path, 'rb')
    
    recipe_obj = Recipe(name=recipe_name)
    recipe_obj.save()
    recipe_obj.img.save(file.split('.')[0]+'.jpg', File(open(image_path, 'rb')))
    for food in data['foods']:
        food_name = food['name']
        '''for ing in food['ings']:
            print('Sub ingredient: '+ing['name'])
            print(ing['ings'].split('|'))'''
        food_ing = convert_dict((food['ings']))
        food_steps = '|'.join(food['steps'])
        food_hints = '|'.join(food['hints'])
        food_portions = food['portions']
            
        #print('Steps: ')
        #print(food['steps'].split('|'))
        #print('Hints: ')
        #print(food['hints'].split('|'))
        food_obj = Food(name=food_name,portions=food_portions,
                        instructions=food_steps,hints=food_hints,
                        ingredients_temp=food_ing)
        food_obj.save()
        recipe_obj.foods.add(food_obj)
        print('{} Food saved'.format(food_name))
    recipe_obj.save()
    print('{} Recipe saved'.format(recipe_name))


class Command(BaseCommand):
    help = 'Imports google drive data to Backend'
    
    def handle(self, *args, **options):
        text_entries = os.listdir(os.path.join(BASE, JSON))

        for text in text_entries:
            if '+' not in text and "Lihapullat ja cajunmaustetut lohkoperunat" in text:
                parseJSON(text)
                print('{} file imported'.format(text))