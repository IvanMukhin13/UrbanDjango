from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_platform, name='index_platform'),
    path('games/', views.index_games, name='index_games'),
    path('cart/', views.index_cart, name='index_cart'),

]