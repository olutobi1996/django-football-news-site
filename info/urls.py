from . import views
from django.urls import path

urlpatterns = [
    path('', views.info, name='info'),
]