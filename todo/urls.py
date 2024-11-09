from django.contrib import admin
from django.urls import path, include
from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskComplete,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "todo"

urlpatterns = [
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task_create/", TaskCreateView.as_view(), name="task-create"),
    path("task_update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task_delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task_complete/<int:pk>/", TaskComplete.as_view(), name="task-complete"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags_create/", TagCreateView.as_view(), name="tag-create"),
    path("tags_update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags_delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]
