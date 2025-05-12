from django.urls import path
from .views import index, TagListView


app_name = "task"

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list")
]