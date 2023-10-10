from django.urls import path
from .views import TaskListAPIView,TaskDetailView,CreateAPIViews,TaskUpdateViews,TaskDeleteViews
from rest_framework.authtoken import views

urlpatterns = [
    path('',TaskListAPIView.as_view(),name='task_list'),
    path('detail-task/<int:pk>/',TaskDetailView.as_view(),name='book_detail'),
    path('create-task/',CreateAPIViews.as_view(),name='create-task'),
    path('update-task/<int:pk>/',TaskUpdateViews.as_view(),name='update-task'),
    path('delete-task/<int:id>',TaskDeleteViews.as_view(),name='delete-task'),
    path('token-auth',views.obtain_auth_token),
    # path('api/?filter='),  To get filter data
]