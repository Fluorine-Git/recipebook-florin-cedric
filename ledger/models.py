from datetime import datetime
from django.db import models
from django.urls import reverse
from accounts.models import Profile

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail')
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="recipe",
        null=True,
    )

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.id)])
    

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name = "recipe")
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name = "ingredients")
