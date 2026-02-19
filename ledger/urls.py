from django.urls import path
from .views import recipe_list, recipe_detail
urlpatterns = [
    path('', recipe_list, name='recipes'),
    path('<int:pk>', recipe_detail, name='recipe_detail'),
]

app_name = "ledger"