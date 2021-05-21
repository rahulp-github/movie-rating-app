from django.contrib import admin
from home.models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display=('id','name','comment','movie_id','movie_name','date')
    
admin.site.register(Review,ReviewAdmin)
