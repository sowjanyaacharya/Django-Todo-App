from django.urls import path
from .import views



urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),   #this is the url for add function
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),    #this is the url for mark_as_done
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),  #this is the url for mark_As_undone
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),  #this is the url for editing the task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),    #this is the url for deleting the task
]