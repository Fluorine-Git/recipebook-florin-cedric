from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.shortcuts import redirect
from .forms import RecipeForm, RecipeImageForm

# Create your views here.

# @login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = { "recipes" : recipes }

    if(request.method == "POST"):
        recipe_form = RecipeForm(request.POST)
        if(recipe_form.is_valid):
            recipe_form.save()
            # recipe = Recipe()
            # recipe.name = recipe_form.cleaned_data["name"]
            # recipe.author = recipe_form.cleaned_data["author"]
            # recipe.save()
            return redirect('/recipes/list')
    return render(request, "recipe_list.html", ctx)

def recipe_add(request):
    authors = Profile.objects.all()
    form = RecipeForm()
    ctx = {
        "authors" : authors,
        "form" : form,
        }
    return render(request, "recipe_add.html", ctx)

def image_add(request, pk):

    if (request.method == "POST"):
        recipe = Recipe.objects.get(pk=pk)
        image_form = RecipeImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.recipe = Recipe.objects.get(pk=pk)
            image.save()
            return redirect(recipe.get_absolute_url())
    else:
        image_form = RecipeImageForm()
        
    ctx = { "form" : image_form }
    return render(request, "image_add.html", ctx)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        "recipe" : recipe,
        }
    return render(request, "recipe_detail.html", ctx)