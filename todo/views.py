from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from todo.models import CreateTodo
from urllib.parse import urlparse, urlunparse
from urllib.parse import urlencode

def index(requests):
    return render(requests, 'index.html')

def signup(request):
    url = request.META.get('HTTP_REFERER', None)
    refering_url = ""
    if url:
        refering_url = url
    else: 
        refering_url = 'index'
    if request.method  == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        #Checks
        if len(password) < 8:
            messages.error(request, 'Password Length too small!')
            print(request.path_info)
            return redirect(refering_url)

        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect(refering_url)
        
        #Creating The User
        user = User.objects.create_user(username = name, email = email, password = password)
        user.save()
        messages.success(request, 'Your account is being created!')
        return redirect(refering_url)

    else:
        return HttpResponse('<h1>404 Page-Not-Found</h1>')

def logIn(request):
    url = request.META.get('HTTP_REFERER', None)
    refering_url = ""
    if url:
        refering_url = url
    else: 
        refering_url = 'index'
    if request.method == "POST":
        LoginName = request.POST['LoginName']
        LoginPassword = request.POST['LoginPassword']
        user = authenticate(username = LoginName, password = LoginPassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logined Succesfully.')
            return redirect(refering_url)

        else:
            messages.error(request, 'Either Username or Password is wrong.')
            return redirect(refering_url)

def logOut(request):
    logout(request)
    messages.success(request, 'LogedOut.')
    return redirect('index')


def createtodo(request):
    return render(request, 'createTodo.html')

def viewTodo(request):
    todos = CreateTodo.objects.all().filter(user_id = request.user.id)
    param = {"todos": todos} 
    return render(request, 'viewTodo.html', param)

    

def saveTodo(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        desc = request.POST['desc']
        expectedDateTime = request.POST['Cdate']
        todo = CreateTodo(title = title, desc = desc, expectedDateTime = expectedDateTime, user = user)
        todo.save()
        return redirect('viewTodo')
    else:
        return HttpResponse('404-Page Not Found!')
    




        
