#from cgitb import lookup
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
#from django.conf import settings
from rest_framework import generics

import json


from .serializers import LightRecipeSerializer, RecipeSerializer, IngredientSerializer
from Recipe.models import Recipe,Ingredient,RecipeIngredient

@api_view(['POST'])
def createRecipe(request):
    print('creating recipe')
    name = request.data.get('name','Untitled recipe')
    details = request.data.get('details','')
    instructions = request.data.get('instructions','')
    tags = request.data.get('tags','')
    #img = request.data.get('img','')
    # generate list of ingredients
    ingredients = json.loads(request.data.get('ingredients','[]'))
    print(ingredients)

    newRecipe = Recipe(
        user=request.user, name=name, details=details, instructions=instructions,
        tags=tags
    )
    newRecipe.save()
    for pairObj in ingredients:
        print('attempting adding ingredient {} with quantity {}'.format(pairObj['name'],pairObj['quantity']))
        ingredient,createdBool = Ingredient.objects.get_or_create(name=pairObj['name'])
        print(type(ingredient))
        recipeIngredient = RecipeIngredient(
            recipe = newRecipe, ingredient = ingredient, quantity=pairObj['quantity']
        )
        recipeIngredient.save()
        newRecipe.ingredients.add(recipeIngredient)

    header = {"status_code": 200}
    return Response({"recipe_id":newRecipe.id},headers=header)


class RecipeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.filter()
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class MyRecipes(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.filter()


@api_view(['POST'])
def createIngredient(request):
    name = request.data.get('name','Untitled ingredient')
    unit = request.data.get('unit','')

    newIngredient = Ingredient(
        name=name, unit=unit
    )
    newIngredient.save()
    
    header = {"status_code": 200}
    return Response({"recipe_id":newIngredient.id},headers=header)


class AllIngredients(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.all()