from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, RecipeIngredient, Food

admin.site.register(Recipe)
admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
