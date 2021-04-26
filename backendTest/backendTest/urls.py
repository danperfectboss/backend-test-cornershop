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

    ##URL for recipes
    path('createRecipe/', views.create_recipes,name="create"),
    path('updateRecipe/<int:param_id_recipes>', views.update_recipes,name="update"),
    path('deleteRecipe/<int:param_id_recipes>', views.delete_recipes,name="delete"),
    path('allRecipes/', views.read_recipes,name="read"),
]
