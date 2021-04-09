from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>', views.delete_widget, name='delete_widget'),
]
