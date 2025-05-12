from django.shortcuts import render
from django.views import generic

from .models import Task, Tag


def index(request):
    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks": tasks,
        "tags": tags,
    }

    return render(request, "task/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag_list.html"
    context_object_name = "tag_list"