from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.

def create_recipes(request):
    
    pass

def update_recipes(request):

    if request.method is "POST":
        pass
    
    pass

def delete_recipes(request,param_id_recipes):
    if request.method is "POST":

        try:
            recipes = Recipe.objects.get(id_recipe=param_id_recipes)
            recipes.delete()
        except:
            message.error(request, "That recipe don't exist")
         
        pass
    pass

def read_recipes(request):

    recipes = Recipe.objects.all()

    return render(request,"recipes/get_allrecipes.html" )
    
    pass




