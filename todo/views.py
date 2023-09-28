from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task

# Create your views here.
def addTask(request):   #performs the add operations here
    task = request.POST['task']   #this is we are reuesting to display the data we entered on the add task 'task' is the input type name
    Task.objects.create(tasks=task)   #in the task model we are creating the new tasks
    return redirect('home')      #render the home page

def mark_as_done(request, pk):       #request task id in the url
    task = get_object_or_404(Task,pk=pk)       #if that pk is present means fetches taht task based on the pk 
    task.is_complete = True    #it assigns the task as completed 
    task.save()     #it saves in the database
    return redirect('home')   #redirects the home page itself

def mark_as_undone(request, pk):   #mark as undone
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = False
    task.save()
    return redirect('home')

def edit_task(request, pk):  #while clicking on edit it performs the actions
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':   # if method is post means update button is used work on serverside
        new_task = request.POST['task']   #it takes input values   
        get_task.tasks = new_task    #assigns in the task object
        get_task.save()             #it saves
        return redirect('home')       #it redirects the home page once when the updation is done
    else:                   #if method is get means it should display the old task in the input field
        context = {
            'get_task' : get_task,

        }
        return render(request, 'edit_task.html', context)   #passing the context
    
def delete_task(request, pk):   #while clicking on delete
    task = get_object_or_404(Task, pk=pk)   #based on id 
    task.delete()    #it deletes the task this is the built in delete method in django
    return redirect('home')   #redirects the home page once the task is deleted

