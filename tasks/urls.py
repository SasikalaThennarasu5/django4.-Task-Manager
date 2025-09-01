from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("add/", TaskCreateView.as_view(), name="task-add"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task-edit"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]
