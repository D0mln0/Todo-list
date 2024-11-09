from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.shortcuts import redirect

from todo.forms import TaskCreateForm
from todo.models import Task, Tag
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(UpdateView):
    form_class = TaskCreateForm
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskComplete(View):
    model = Task

    def post(self, request, pk, *args, **kwargs):
        task = self.model.objects.get(id=pk)
        task.completed = not task.completed
        task.save()
        return redirect("todo:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "tag_list.html"
    ordering = ["name"]


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
