from django.shortcuts import render

from .models import Task, Tag


def index(request):
    task = Task.objects.all()
    tag = Tag.objects.all()

    context = {
        "task": task,
        "tag": tag,
    }

    return render(request, "task/index.html", context=context)