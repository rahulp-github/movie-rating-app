from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import requests


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
    url = 'http://www.omdbapi.com/?apikey=d61c5b45&i='+id
    response = requests.get(url)
    data = response.json()
    return render(request,'final.html',{'data':data})

def about(request):
    return render(request,'about.html')

