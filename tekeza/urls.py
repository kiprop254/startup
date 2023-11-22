from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tekeza-home'),
    path('about/', views.about, name='tekeza-about'),
]
