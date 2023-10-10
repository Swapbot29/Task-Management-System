from django.urls import path
from .views import TaskListView,TaskCreate,DeleteView,TaskUpdate

urlpatterns = [
    path('',TaskListView.as_view(),name='home'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',DeleteView.as_view(),name='task-delete'),
]