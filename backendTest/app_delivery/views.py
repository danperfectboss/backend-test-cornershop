from django.http import request
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib import messages
from .complements.dates import Transformdata
from .complements.bot import *

# Create your views here.

def create_recipes(request):
    if request.method == "POST":
        try:
            menu = request.POST.get('menu')
            date = str(request.POST.get('date'))
            dateObj =  Transformdata(date).transform_date()
            if Transformdata(dateObj).validate_date():
            
                recipes = Recipe(description=menu,date=dateObj)
                recipes.save()
                messages.success(request,"Receta agregada exitosamente")
               
            else:
                messages.error(request,"No puedes agregar una receta que sea anterior al día de hoy")
                
            
        except:
            return HttpResponseBadRequest('Por el momento no podemos guardar la receta')

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
            messages.success(request,"La receta se edito correctamente")
        except:
            messages.error("No se pudo editar la receta")
        
        return HttpResponseRedirect("/updateRecipe/"+str(param_id_recipes))
    else:
        
        if type(param_id_recipes) is int:
            unique_recipe = Recipe.objects.get(id_recipe=param_id_recipes)
            if unique_recipe is None:
                return HttpResponse("Receta no encontrada")
            else: 
                unique_recipe.date = unique_recipe.date.strftime("%d/%m/%y")
                return render(request, "recipes/edit_recipes.html",{"recipe":unique_recipe})



def delete_recipes(request,param_id_recipes):
   

    try:
        recipes = Recipe.objects.get(id_recipe=param_id_recipes)
        recipes.delete()
        messages.success(request,"Receta eliminada correctamente")
    except:
        messages.error(request, "Esta receta no existe")

    return HttpResponseRedirect("/allRecipes/")
    

def read_recipes(request):

    recipes = Recipe.objects.all()

    return render(request,"recipes/get_allrecipes.html",{'recipes':recipes} )





def index(request):
    return HttpResponseRedirect("/menu/")


def menu(request,param_id_recipes):
    # try:
    #     Recipe.object

    # if request.method == "POST":
    #     pass
    # else:
    #     return HttpResponseRedirect("/menu/"+str(param_id_recipes))
    pass

def disable_recipe(request):
    pass

def enable_recipes(request,param_id_recipes):
    #In this method send the menssage to slack channel and enable the recipe for the method
    try:
        recipe=Recipe.objects.get(id_recipe=param_id_recipes)
        recipe.public = True
        recipe.save()
        # Bot_Slack("http://127.0.0.1:8000/menu/"+str(param_id_recipes)).send_message("_")

        send_message("http://127.0.0.1:8000/menu/"+str(param_id_recipes))
        
        messages.success(request,"Receta publicada correctamente")
        
    except:
        return HttpResponse("No se habilito la nota")

    return render(request, "get_allrecipes.html")
    