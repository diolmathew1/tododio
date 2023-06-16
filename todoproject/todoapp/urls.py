from django.contrib import admin
from django.urls import path
from todoapp import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.tasksindex, name='taskslist'),
    path('add/', views.task_add, name='taskadd'),
    path('delete/<int:taskid>', views.deletee, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='tasklistview'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='taskdetailview'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='taskupdateview'),
path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='taskdeleteview'),

]
