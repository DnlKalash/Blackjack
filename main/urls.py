from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.htmlshablon, name='htmlshablon'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),  
    path('logout/', views.logout, name='logout'),
]
