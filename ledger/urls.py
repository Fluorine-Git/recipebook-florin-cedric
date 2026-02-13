from django.urls import path
from .views import recipes, recipe_1, recipe_2

urlpatterns = [
    path('list', recipes, name='recipes'),
    path('1', recipe_1, name='recipe1'),
    path('2', recipe_2, name='recipe2')
]

app_name = "ledger"