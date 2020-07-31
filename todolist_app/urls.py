from todolist_app import views
from django.urls import path

urlpatterns = [
    
    path('',views.todolist,name='todolist'),
    path('delete/<task_id>',views.delete_task,name='delete_task'),
    path('edit/<task_id>',views.edit,name='edit'),
    path('complete/<task_id>',views.complete,name='complete'),
    path('pending/<task_id>',views.pending,name='pending')
]
