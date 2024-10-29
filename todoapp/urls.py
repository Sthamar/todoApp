from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.signupuser, name='signupuser' ),
    path('home/', views.home, name='home' ),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name='loginuser'),
    path('create/', views.createtodo, name="create"),
    path('todo_list/', views.todoList, name="todo_list"),
    path('todo/<int:id>', views.todopage, name='todopage'),
    path('complete/', views.complete, name='complete'),
    path('todo/<int:id>/delete/', views.deletetodo, name='deletetodo')
]
