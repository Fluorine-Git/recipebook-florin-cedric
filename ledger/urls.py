from django.urls import path, include
from .views import *
urlpatterns = [
    path('recipes/list', recipe_list, name='recipes'),
    path('recipe/<int:pk>', recipe_detail, name='recipe_detail'),
    path('recipe/add', recipe_add, name="recipe_add"),
    path('recipe/<int:pk>/add_image/', image_add, name="image_add"),
]

app_name = "ledger"