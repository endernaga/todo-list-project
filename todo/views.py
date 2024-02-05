from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.models import Task, Tags


class TodoListView(ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 5
    template_name = "todo/index.html"


class TodoCreateView(CreateView):
    model = Task
    fields = ("content", "tags")
    success_url = reverse_lazy("todo:index")


class TodoUpdateView(UpdateView):
    model = Task
    fields = ("content", "tags")
    success_url = reverse_lazy("todo:index")


class TodoDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagsListView(ListView):
    model = Tags
    context_object_name = 'tags'
    paginate_by = 5


class TagsCreateView(CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")


class TagsUpdateView(UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")


class TagsDeleteView(DeleteView):
    model = Tags


class ChangeFinishedViewStatus(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        task = Task.objects.get(pk=pk)
        task.finished = not task.finished
        task.save()
        return redirect("todo:index")
