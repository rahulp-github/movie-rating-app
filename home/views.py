from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from home.models import Review
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate,login, logout
from .models import WatchList

# home function renders home page 
def home(request):
    
    return render(request,'index.html')


# This function fetch the details of all movies
# using API key and passes to the template
def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        url = 'http://www.omdbapi.com/?apikey=d61c5b45&s='+ query
        response = requests.get(url)
        data = response.json()
        isTrue = data['Response'].lower()
        if isTrue == "true":
            return render(request,'search.html',{'data':data,'query':query})
        else:
            return render(request,'error.html',{'query':query})
        
    return render(request,'index.html')
 
# This Function displays the Movie Details and also stores
# Comment Details for the Movie
def movieDetails(request,id):
    obj = Review()
    url = 'http://www.omdbapi.com/?apikey=d61c5b45&i='+id
    response = requests.get(url)
    data = response.json()
    showWatchListOption =True
    if request.user.is_authenticated :
          user = request.user
          watchList_details = WatchList.objects.filter(user = user,movie_id = id)
          if len(watchList_details) >= 1:
              showWatchListOption = False
    
    comments = Review.objects.all().filter(movie_id=id)
    comment_found = True
    if len(comments) == 0:
        comment_found = False

    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.comment = request.POST.get('comment')
        obj.movie_id = id
        obj.movie_name = data['Title']
        obj.save()
        messages.success(request,'Thanks for The Comment !!')
        return redirect('/id/'+id) 
    return render(request,'final.html',{'data':data,'comments':comments,'comment_found':comment_found,'length':len(comments),'watchListOption':showWatchListOption})

# Renders The About template
def about(request):
    return render(request,'about.html')


# Signin
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            msg  = 'Login Successful !! Hello, ' + user.get_username().capitalize()
            messages.info(request,msg)
            return redirect('/')
        else:
            messages.warning(request,'Password OR Username Error !!')
            return redirect('/signin/')

    return render(request,'signin.html')

# Signup
def signup(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=name)
            user.save()
        except IntegrityError as e: 
            messages.warning(request,'Username already exists Try Different username')
            return redirect('/signup/')
        messages.success(request,"Signup Successful, Login With your username and Password")
        return redirect('/signin/')
        
    return render(request,'signup.html')

# logout
def user_logout(request):
    logout(request)
    return redirect('/')


# WatchList
def watch_list(request,id,movie_name,year):
    obj = WatchList()
    user = request.user
    obj = WatchList(user=user,movie_name=movie_name,movie_year=year,movie_id=id)
    obj.save()
    messages.success(request,'Added To Your Watch List SuccessFully !! ')
    return redirect('/id/' + id)