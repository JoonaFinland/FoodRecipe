from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Recipe.models import *

User = get_user_model()

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id']
        read_only_fields = []


class LightRecipeSerializer(serializers.ModelSerializer):
    #user = UserViewSerializer(many=False)
    class Meta:
        model = Recipe
        exclude = ['foods']


class XLightRecipeSerializer(serializers.ModelSerializer):
    #user = UserViewSerializer(many=False)
    class Meta:
        model = Recipe
        fields = ['name','id',]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False)
    class Meta:
        model = RecipeIngredient
        fields = ['quantity','ingredient']

class FoodSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)
    class Meta:
        model = Food
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    #user = UserViewSerializer(many=False)
    foods = FoodSerializer(many=True)
    class Meta:
        model = Recipe
        fields = '__all__'