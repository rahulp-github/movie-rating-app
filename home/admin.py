from django.contrib import admin
from home.models import Review,WatchList
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display=('id','name','comment','movie_id','movie_name','date','time')

class WatchListAdmin(admin.ModelAdmin):
    list_display=('user','movie_id','movie_name','movie_year')
    
admin.site.register(Review,ReviewAdmin)
admin.site.register(WatchList,WatchListAdmin)
