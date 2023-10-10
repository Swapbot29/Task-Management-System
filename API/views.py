from django.shortcuts import render
from rest_framework import generics
from task.models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.filters import SearchFilter

# Create your views here.

class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^status','due_date','team_member']

class TaskDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateAPIViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,IsAuthenticated]
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.data,status=status.HTTP_401_BAD_REQUEST)

class TaskUpdateViews(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskDeleteViews(APIView):
    def delete(self,request,id=None):
        task_data = Task.objects.filter(id=id)
        if task_data:
            task_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)