from webbrowser import get
from django.urls import re_path as url
from .views import *

app_name = "api-recipe"

urlpatterns = [
    # RECIPE URLS
    url(r'^recipe/create$', createRecipe, name="create_recipe"),
    url(r'^recipe/(?P<id>\d+)$', RecipeRudView.as_view(), name="recipe_rud"),
    url(r'^recipe/all$', MyRecipes.as_view(), name="all_recipes"),
    # INGREDIENT URLS
    url(r'^ingredient/create$', createIngredient, name="create_ingredient"),
    url(r'^ingredient/all$', AllIngredients.as_view(), name="get_ingredients"),
]