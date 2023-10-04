from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.logIn, name = 'logIn'),
    path('logout', views.logOut, name = 'logOut'),
    path('signUp', views.signup, name = 'signup'),
    path('createtodo/', views.createtodo, name = 'createtodo'),
    path('viewTodo/', views.viewTodo, name = 'viewTodo'),
    path('saveTodo/', views.saveTodo, name = 'saveTodo')
]