from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
import random

# Create your views here.

def top250(request):
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')

    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    movie_id = []
    for id in links:
        movie_id.append(id[7:16])
        
    ratings = [b.attrs.get('data-value')
    for b in soup.select('td.posterColumn span[name=ir]')]

    movie_rating = []
    for rating in ratings:
        rating = float(rating)
        movie_rating.append(round(rating,2))

    movie_title = []
    movie_year = []
    for i in range(0,len(movies)):
        movie_string = movies[i].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        year = re.search('\((.*?)\)', movie_string).group(1)
        movie_title.append(movie[len(str(i))+1:-7])
        movie_year.append(year)
    data = zip(movie_title,movie_rating,movie_year,movie_id)
    return render(request,'top250.html',{'data':data})

def top10(request):
    movie_title = ['Kota Factory','TVF Pitchers','The Family Man','Sacred Games','Special OPS','Asur','Mirzapur','Breathe','Apharan','Paatal lok']
    movie_rating = [9.2,9.1,8.6,8.6,8.6,8.5,8.4,8.3,8.3,7.8]
    movie_id = ['tt9432978','tt4742876','tt9544034','tt6077448','tt11854694','tt11912196','tt6473300','tt6466208','tt8392006','tt9680440']
    movie_year = ['2019','2015','2019','2018-2019','2020','2020','2018','2018','2018','2020']
    data = zip(movie_title,movie_rating,movie_year,movie_id)
    return render(request,'top10.html',{'data':data})

def top_box_office(request):
    url = 'https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    revenue_weekend = []
    revenue_gross = []
    weeks = []
    movie_title = []
    movie_id = []
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
   
    for id in links:
        id.replace('/',"")
        movie_id.append(id[7:])
    
    week = soup.select('td.weeksColumn')
    for i in week:
        weeks.append(i.get_text())
    weekend = soup.select('td.ratingColumn')
    j = 0
    for i in range(0,len(weekend)):
        string = weekend[i].get_text()
        r = (' '.join(string.split()).replace(' ', ''))
        if j % 2 == 0:
            revenue_weekend.append(r)
        else:
            revenue_gross.append(r)
        j += 1
   
    title = soup.select('td.titleColumn a')
    for i in title:
        movie_title.append(i.get_text())
    data = zip(movie_title,revenue_weekend,revenue_gross,weeks,movie_id)
    return render(request,'boxoffice.html',{'data':data})






    


