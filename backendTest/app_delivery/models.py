from django.db import models

# Create your models here.

class Recipe(models.Model):
    id_recipe = models.AutoField(primary_key=True)
    description = models.CharField(max_length=700)
    date = models.DateField(auto_now=False, auto_now_add=False)

class Employees(models.Model):
    id_employee = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=400)
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)