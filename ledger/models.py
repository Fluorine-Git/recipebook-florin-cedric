from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])
    

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
