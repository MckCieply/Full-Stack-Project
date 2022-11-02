from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/roccodeals/', views.roccodeals, name='roccodeals'),
    path('/lancerdeals/', views.lancerdeals, name='lancerdeals'),
]