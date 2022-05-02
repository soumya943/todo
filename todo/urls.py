from django.urls import path
from django.conf.urls import url
from .views import TodoApiView, TodoApiDeleteView
from todo import views


urlpatterns = [
    path('', TodoApiView.as_view(), name="todoAPI"),
    path('api/delete/<str:gid>', TodoApiDeleteView.as_view(), name="todoAPI"),
    path('Todo/',views.TodoApiView.as_view()),
]
