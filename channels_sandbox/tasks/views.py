from django.shortcuts import render


def index(request):
    return render(request, 'tasks/tasks_list.html', {})


def tasks_list(request):
    return
