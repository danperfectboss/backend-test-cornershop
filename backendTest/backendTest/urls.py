"""backendTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_delivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),


    ##URL for recipes
    path('createRecipe/', views.create_menu,name="create"),
    path('updateRecipe/<int:param_id_menu>', views.update_menu,name="update"),
    path('deleteRecipe/<int:param_id_menu>', views.delete_menu,name="delete"),
    path('allRecipes/', views.read_menu,name="read"),
    
    path('enable/<int:param_id_menu>', views.enable_menu,name="enable"),
    path('menu/<int:param_id_menu>', views.menu,name="menu"),
    path('customMenu/', views.read_custom_menu,name="custom"),
    path('deleteCustomMenu/<int:param_id_menu>', views.delete_custom_menu,name="custom"),
    # deleteCustomMenu



]
