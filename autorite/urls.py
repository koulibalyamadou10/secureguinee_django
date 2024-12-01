from django.urls import path, include

from . import views

urlpatterns = [
    path('autorite', views.autorite, name='autorite'),
    path('add_autorite', views.add_autorite, name='add_autorite'),
    path('autorites', views.autorites, name='autorites'),
    path('login', views.login, name='login'),
]
