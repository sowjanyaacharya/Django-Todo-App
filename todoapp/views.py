#from django.http import HttpResponse    # this is the created view we are importing the httpresponse
from django.shortcuts import render   #this is to render the html page
from todo.models import Task   # importing ftask models from todo we are going to import task
#creating the home function
def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')  #order_by clause is used to fetch the data in asc...order if we put'hyphenupdate_at' it will be in des... #fetching the tasks which are incomplete getting the lists
    #print(tasks) so here task is the class name filtering the multiple data ,get is used to fetch single data and all is used to fetch all the data
    completed_task = Task.objects.filter(is_complete=True).order_by('-updated_at')  #fetching of completed task
    #print(completed_task)
   
    context = {
        'tasks' : tasks,
        'completed_task' : completed_task,   #passing to the html page
        #here 'tasks'==>is the main thing we are using  inside the html templates
    }
    return render(request,'home.html',context)