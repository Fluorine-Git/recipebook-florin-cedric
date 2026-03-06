from django.urls import path, include
from .views import recipe_list, recipe_detail
urlpatterns = [
    path('recipes/', recipe_list, name='recipes'),
    path('recipe/<int:pk>', recipe_detail, name='recipe_detail'),
]

app_name = "ledger"