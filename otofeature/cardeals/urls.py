from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roccodeals/', views.roccodeals, name='roccodeals'),
    path('lancerdeals/', views.lancerdeals, name='lancerdeals'),
]