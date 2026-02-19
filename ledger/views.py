from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes" : recipes}
    return render(request, "recipe.html", ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = { "recipe" : recipe }
    return render(request, "recipe_detail.html", ctx)