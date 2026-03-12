from django import forms
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient
from accounts.models import Profile

class RecipeForm(forms.ModelForm):
    name = forms.CharField(label="Recipe Name", max_length=100)
    author = forms.ModelChoiceField(
        label = "Author",
        queryset = Profile.objects.all()
    )

    class Meta:
        model = Recipe
        fields = "__all__"

class RecipeImageForm(forms.ModelForm):
    image = forms.ImageField(label="Image:")
    description = forms.CharField(label="Description:")

    class Meta:
        model = RecipeImage
        fields = ["image", "description"]