from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
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


def toggle_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("task:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "task_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("task:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")