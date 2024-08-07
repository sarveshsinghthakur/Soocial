from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('<str:slug>/', views.room, name='room'),
    path('create-room/', views.create_room, name='create-room'),
    path('auth/login/', LoginView.as_view(template_name='chat/loginpage.html'), name='login-user'),
    path('auth/logout/', LogoutView.as_view(), name='logout-user'),
]
