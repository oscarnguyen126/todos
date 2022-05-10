from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from django.http import JsonResponse


def listtodo(request):
    todos = [TodoSerializer(todo).parse() for todo in Todo.objects.all()]
    return JsonResponse({'todos': todos})


def detailtodo(request, id):
    todos = [TodoSerializer(todo).parse()
             for todo in Todo.objects.filter(id=id)]
    return JsonResponse({'todos': todos})
