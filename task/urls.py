from django.urls import path
from .views import index, toggle_task_done, TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView


app_name = "task"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/<int:pk>/toggle_done/", toggle_task_done, name="task-toggle-done"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]