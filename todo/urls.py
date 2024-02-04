from django.urls import path

from todo.views import TodoListView, TagsListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TagsCreateView, \
    TagsUpdateView, TagsDeleteView, change_finished_status

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("todo/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>/update", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>/delete", TodoDeleteView.as_view(), name="todo_delete"),
    path("todo/<int:pk>/status", change_finished_status, name="status_update"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create/", TagsCreateView.as_view(), name="tags_create"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tags_update"),
    path("tags/<int:pk>/delete", TagsDeleteView.as_view(), name="tags_delete")
]

app_name = "todo"
