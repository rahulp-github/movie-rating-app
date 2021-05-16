from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from home.models import Review

def home(request):
    return render(request,'index.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        url = 'http://www.omdbapi.com/?apikey=d61c5b45&s='+query
        response = requests.get(url)
        data = response.json()
        isTrue = data['Response'].lower()
        if isTrue == "true":
            return render(request,'search.html',{'data':data,'query':query})
        else:
            return render(request,'error.html',{'query':query})
        
    return render(request,'index.html')
 

def movieDetails(request,id):
    obj = Review()
    url = 'http://www.omdbapi.com/?apikey=d61c5b45&i='+id
    response = requests.get(url)
    data = response.json()
    comments = Review.objects.all().filter(movie_id=id)
    comment_found = True
    if len(comments) == 0:
        comment_found= False
    
    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.comment = request.POST.get('comment')
        obj.movie_id = id
        obj.movie_name = data['Title']
        obj.save()
        # comments = Review.objects.all().filter(movie_id=id)
        # #return render(request,'final.html',{'data':data,'comments':comments,'comment_found':True,'length':len(comments)})
        return redirect('/id/'+id)
    return render(request,'final.html',{'data':data,'comments':comments,'comment_found':comment_found,'length':len(comments)})

def about(request):
    return render(request,'about.html')


