"""
URL configuration for space_catalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('spaceobjects/', views.spaceobject_list, name='spaceobject_list'),
    path('spaceobject/<int:id>/', views.spaceobject_detail, name='spaceobject_detail'),
    path('spaceobject/<int:id>/notes/', views.notes_list, name='notes_list'),
    path('spaceobject/<int:id>/notes/add/', views.create_note, name='create_note'),
    path('spaceobject/<int:id>/notes/<int:note_id>/edit/', views.update_note, name='update_note'),
    path('spaceobject/<int:id>/notes/<int:note_id>/delete/', views.delete_note, name='delete_note'),
]


