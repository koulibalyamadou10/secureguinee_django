from django.urls import path, include

from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('add_user', views.add_user, name='add_user'),
    path('users', views.users, name='add_user'),
    path('login', views.login, name='login'),
    path('test', views.test, name='test'),
    path('upload', views.upload_image, name='upload'),
    path('sgusers/', views.user, name='scusers'),
]
