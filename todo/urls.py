from django.urls import path
from .import views

app_name = 'todo'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('done/<int:todo_id>', views.doneTodo, name='done'),
    path('update/<pk>', views.UpdateTodoView.as_view(), name='update'),
    path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
]
