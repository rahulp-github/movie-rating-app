from django.core.checks import messages
from django.shortcuts import redirect, render
from home.models import WatchList
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='/signin/')
def your_watchlist(request):
    obj = WatchList()
    user = request.user
    data = WatchList.objects.filter(user=user)
    count = len(data)
    if len(data) == 0:
        isNull = "yes"
    else:
        isNull = "no"
    return render(request,'watchlist.html',{'data':data,'isNull':isNull,'count':count})


def delrecord(request,id):
    user = request.user
    data = WatchList.objects.filter(user=user,movie_id =id).delete()
    messages.info(request, 'Deleted from your Watchlist Successfully!!')
    return redirect('/yourWatchlist/')
