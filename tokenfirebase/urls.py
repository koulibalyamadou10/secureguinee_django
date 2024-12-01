from django.urls import path, include

from . import views

urlpatterns = [
    path('update_token_firebase', views.update_token_firebase, name='update_token_firebase'),
]
