from django.db import models
from django.conf import settings

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    unit = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe',on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient',on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=1,max_digits=10)

    def __str__(self):
        return self.recipe.name + '_' + self.ingredient.name +\
            '_(' + str(self.quantity) + ')'


class Recipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=120,blank=True, default='')
    instructions = models.TextField(blank=True, default='')
    tags = models.TextField(blank=True, default='')
    img = models.ImageField(upload_to='photos/', blank=True)
    ingredients = models.ManyToManyField(RecipeIngredient, blank=True, related_name='ingredient_in_recipe')

    def __str__(self):
        return '_'.join([self.user.username,self.name])