from django.db import models

# Create your models here.

class Recipe(models.Model):
    id_recipe = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=False)

class Employees(models.Model):
    id_employee = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=400)
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class CustomRecipes(models.Model):
    id_customRecipe = models.BigAutoField(primary_key=True)
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    id_employe = models.ForeignKey(Employees, on_delete=models.CASCADE)
    commentary  = models.CharField(max_length=500)