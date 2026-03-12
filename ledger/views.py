from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

# Create your views here.

# @login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = { "recipes" : recipes }
    if(request.method == "POST"):
        r = Recipe()
        r.name = request.POST.get('recipe_name')
        author_primary_key = request.POST.get('recipe_author')
        r.author = Profile.objects.get(pk=int(author_primary_key))
        r.save()
        return render(request, "recipe_list.html", ctx)
    else:
        return render(request, "recipe_list.html", ctx)

def recipe_add(request):
    authors = Profile.objects.all()
    ctx = { "authors" : authors }
    return render(request, "recipe_add.html", ctx)

def image_add(request):
    images = RecipeImage.objects.all()
    ctx = { "images" : images }
    return render(request, "image_add.html", ctx)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        "recipe" : recipe,
        }
    return render(request, "recipe_detail.html", ctx)