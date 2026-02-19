from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_lenght=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name = "recipe")
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name = "ingredients")
    
    class Meta:
