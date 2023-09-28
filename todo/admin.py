from django.contrib import admin
from .models import Task

# Register your models here.
#we are overriding the admin model==>(this is to display the table with columns created at,is_complete,task)
class Taskadmin(admin.ModelAdmin):
    list_display = ('tasks','is_complete','created_at')
    search_fields = ('tasks',)   #this is to display the search bar thes are the attributes which are built in


admin.site.register(Task,Taskadmin)   #passing overriden tables
