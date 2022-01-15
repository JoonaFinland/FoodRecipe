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
    user = UserViewSerializer(many=False)
    class Meta:
        model = Recipe
        exclude = ['instructions']


class XLightRecipeSerializer(serializers.ModelSerializer):
    user = UserViewSerializer(many=False)
    class Meta:
        model = Recipe
        fields = ['user','name','id',]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False)
    recipe = XLightRecipeSerializer(many=False)
    class Meta:
        model = RecipeIngredient
        fields = ['quantity','ingredient','recipe']


class RecipeSerializer(serializers.ModelSerializer):
    user = UserViewSerializer(many=False)
    ingredients = RecipeIngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = '__all__'