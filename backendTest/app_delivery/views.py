from django.http import request
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib import messages
from .complements.dates import Transformdata
from .complements.bot import *


'''#Función que crea el menu y lo guarda en la base de datos'''
def create_menu(request):
    #Si viene de un metodo post guarda la información en la base de datos
    if request.method == "POST":
        try:
            menu = request.POST.get('menu')
            date = str(request.POST.get('date'))
            #Convierte la fecha ingresada por el usuario en un obj tipo datetime
            dateObj =  Transformdata(date).transform_date()
            #Se valida que no ingrese una fecha anterior al día en que se esta gerando el registro
            if Transformdata(dateObj).validate_date():
            
                newMenu = Recipe(description=menu,date=dateObj)
                #guarda el menu en base de datos
                newMenu.save()
                messages.success(request,"Receta agregada exitosamente")
               
            else:
                messages.error(request,"No puedes agregar un menu que sea anterior al día de hoy")
                
            
        except:
            return HttpResponseBadRequest('Por el momento no podemos guardar el menu')

        #Retorna a la página de agregar archivo
        return render(request,'recipes/add_recipes.html')
    else:
        return render(request, 'recipes/add_recipes.html')


'''Metódo que actualza la información existen de un Menu en la base de datos
Recibe como datos el request y el id del elemento a editar'''
def update_menu(request, param_id_menu):

    if request.method == "POST":
        # Obtiene los datos por medio del request y asi integrarlos a la base de datos
        menu = request.POST.get('menu')
        date = str(request.POST.get('date'))
        
        try:
            #Recupera el elemnto a editar, asigna los parametros recibidos y guarda
            editMenu = Recipe.objects.get(id_recipe=param_id_menu)
            editMenu.description = menu
            editMenu.date = Transformdata(date).transform_date()
            editMenu.save()
            messages.success(request,"El menu se edito correctamente")
        except:
            messages.error("No se pudo editar el Menu")
        
        return HttpResponseRedirect("/updateRecipe/"+str(param_id_menu))
    else:
        # Siel request es de tipo GET se recupera el elemento con el ID para mostrarlo en el apartado de vistas
        #Se valida el tipo de entrada ya que el parametro a recibir es un entero
        if type(param_id_menu) is int:
            unique_menu = Recipe.objects.get(id_recipe=param_id_menu)
            if unique_menu is None:
                return HttpResponse("Receta no encontrada")
            else: 
                #regresa el menu con la fecha como fue ingresada
                unique_menu.date = unique_menu.date.strftime("%d/%m/%y")
                return render(request, "recipes/edit_recipes.html",{"recipe":unique_menu})


# Función que elimina el menu solicitado
def delete_menu(request,param_id_menu):
   
    try:
        #recupera el elemento por medio del parametro del ID y procese a su eliminación
        menus = Recipe.objects.get(id_recipe=param_id_menu)
        menus.delete()
        messages.success(request,"Receta eliminada correctamente")
    except:
        messages.error(request, "Este menu no existe")
    #retorna a la lista de todas las recetas
    return HttpResponseRedirect("/allRecipes/")
    
#Este metodo recupera todos los menus
def read_menu(request):
    menu = Recipe.objects.all()
    return render(request,"recipes/get_allrecipes.html",{'recipes':menu} )

#Recupera todas los menus personalizados
def read_custom_menu(request):

    #Se genera una lista donde se recuperarán los elementos 
    emploList=list()
    menuList=list()
    noData=False
    #Recupera los menus customizados 
    customMenu = CustomRecipes.objects.all()

    #si no existe ninguno, prende la bandera de noData para mostrar un mensaje en el front
    if len(customMenu) == 0:
        noData = True
    #Se crea una lista con los id existentes para empleados y menus
    for item in customMenu:
        emploList.append(Employees.objects.get(id_employee=item.id_employe.id_employee).name)
        menuList.append(Recipe.objects.get(id_recipe=item.id_recipe.id_recipe).description)
    
    return render(request, "recipes/customsMenu.html", {'customMenu':customMenu,'employee':emploList,'menu':menuList,'noData':noData})

# Función que borra los menus customizados
def delete_custom_menu(request, param_id_menu):
    try:
        custom= CustomRecipes.objects.get(id_customRecipe=param_id_menu)
        custom.delete()
        return HttpResponseRedirect('/customMenu/')
    except:
        return HttpResponse("No se pudo eliminar")



#Envia el Menu y permite la edición del mismo
def menu(request,param_id_menu):
    #Esta bandera es la que se encarga de permitir o el envio del menu customizado antes de las 11 de la mañana
    isEnable = True
    
    #Condición si pasa de las 11 deshabilitar el menu
    #Esta condición toma la hora actual y si es mayor a 11 cambia la badera a False para que nadie pueda enviar recetas despues de eso
    if Transformdata().validate_hour:
        isEnable=False

    
    if request.method == "POST":
        #Recibe los valores para el menu customizado
        name = request.POST.get("name")
        comment =request.POST.get("comment")

        try:
            #guarda el objeto de menu customizado en la base de datos 
            menu= Recipe.objects.get(id_recipe=param_id_menu)
            #Guarda al empleado que genero el comentario
            employee = Employees(name=name, id_recipe=menu)
            employee.save()
            
            #Guarda el menu customizada
            menuCustom = CustomRecipes(id_recipe=menu,id_employe=employee,commentary=comment)
            menuCustom.save()
            #envia mensaje al front
            messages.success(request, "Menu personalizado enviado a Nora")
        except:
            messages.success(request, "No se envio menu personalizado enviada a Nora")


    else:
        #si el request es GET recupera el elemento con el ID solicitado 
        try:
            menu = Recipe.objects.get(id_recipe=param_id_menu)
            
            
        except:
            return HttpResponse("No se pudo recuperar el menú")
    
    return render(request,'recipes/menu.html',{'menu':menu, 'Enable':isEnable})

#Este metodo se encarga de cambiar la bandera dentro del modelo y de disparar el envio de mensaje a Slack
def enable_menu(request,param_id_menu):
    
    try:
        #recibe el id del menu que se va a enviar
        recipe=Recipe.objects.get(id_recipe=param_id_menu)
        recipe.public = True
        recipe.save()
        # Bot_Slack("http://127.0.0.1:8000/menu/"+str(param_id_menu)).send_message("_")

        #se invoca la función para el envio de mensajes al canal de slack parando la ruta por la cual se accederá al menu
        send_message("http://127.0.0.1:8000/menu/"+str(param_id_menu))
        
        messages.success(request,"Receta publicada correctamente")
        
    except:
        return HttpResponse("No se habilito la nota")

    return HttpResponseRedirect('/allRecipes/')

#Metodo se encarga de redireccionar al menu si se visita la raiz de la pagina
def index(request):
    return HttpResponseRedirect("/menu/1")