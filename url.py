from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/students/', views.get_students, name='get_students'),
]