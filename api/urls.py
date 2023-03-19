from django.urls import path
from . import views

urlpatterns = [
    path('all', views.getAll, name='getAll'),
    path('update', views.update, name='update')
]