from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib import messages
from .complements.dates import Transformdata

# Create your views here.

def create_recipes(request):
    if request.method == "POST":
        try:
            menu = request.POST.get('menu')
            date = str(request.POST.get('date'))
            dateObj =  Transformdata(date).transform_date()
            recipes = Recipe(description=menu,date=dateObj)
            recipes.save()
            messages.success(request,"Recipe added successfully")

            
        except:
            return HttpResponseBadRequest('We can´t get the recipes')

        return render(request,'recipes/add_recipes.html')
    else:
        return render(request, 'recipes/add_recipes.html')


def update_recipes(request, param_id_recipes):

    if request.method == "POST":
        menu = request.POST.get('menu')
        date = str(request.POST.get('date'))
        
        try:
            recipes = Recipe.objects.get(id_recipe=param_id_recipes)
            recipes.description = menu
            recipes.date = Transformdata(date).transform_date()
            recipes.save()
            messages.success(request,"The recipes was edit successfuly")
        except:
            messages.error("Can not edit that recipe")
        
        return HttpResponseRedirect("/updateRecipe/"+str(param_id_recipes))
    else:
        
        if type(param_id_recipes) is int:
            unique_recipe = Recipe.objects.get(id_recipe=param_id_recipes)
            if unique_recipe is None:
                return HttpResponse("Recipe not found")
            else: 
                unique_recipe.date = unique_recipe.date.strftime("%d/%m/%y")
                return render(request, "recipes/edit_recipes.html",{"recipe":unique_recipe})



def delete_recipes(request,param_id_recipes):
   

    try:
        recipes = Recipe.objects.get(id_recipe=param_id_recipes)
        recipes.delete()
        messages.success(request,"Recipe deleted successfully")
    except:
        messages.error(request, "That recipe don't exist")

    return HttpResponseRedirect("/allRecipes/")
    

def read_recipes(request):

    recipes = Recipe.objects.all()

    return render(request,"recipes/get_allrecipes.html",{'recipes':recipes} )






