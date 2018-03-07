from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ToDoSerializer
from .models import ToDo

class ToDoListView(APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQEUST)


class ToDoDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()
        return Response("Deleted")


def index(request):
    return render(request, 'catalog/index.html')
