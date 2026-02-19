from django.urls import path
from .views import recipes, recipe_1, recipe_2

urlpatterns = [
    path('recipes', recipes, name='recipes'),
    path('recipe/1', recipe_1, name='recipe1'),
    path('recipe/2', recipe_2, name='recipe2')
]

app_name = "ledger"