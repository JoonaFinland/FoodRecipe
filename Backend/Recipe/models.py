from django.db import models
from django.conf import settings

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    unit = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey('Ingredient',on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.ingredient.name +\
            '_(' + str(self.quantity) + ')'

class Food(models.Model):
    name = models.CharField(max_length=64)
    time = models.IntegerField(blank=False, default=20)
    portions = models.CharField(max_length=12,blank=False, default='1')
    details = models.CharField(max_length=256,blank=True, default='')
    instructions = models.TextField(blank=True, default='')
    hints = models.TextField(blank=True, default='')
    ingredients = models.ManyToManyField(RecipeIngredient, blank=True, related_name='ingredient_in_food')
    ingredients_temp = models.TextField(blank=True, default='')
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    # time from both foods added together
    # portions logic TOD
    tags = models.TextField(blank=True, default='')
    img = models.ImageField(upload_to='photos/', blank=True)
    foods = models.ManyToManyField(Food, blank=True, related_name='food_in_recipe')

    def __str__(self):
        return '_'.join([self.name])