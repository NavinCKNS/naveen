
from django.urls import path
from B import views

urlpatterns = [
    path('', views.login),
]
