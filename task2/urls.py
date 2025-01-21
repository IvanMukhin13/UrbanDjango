from django.urls import path
from . import views

urlpatterns = [
    path('class/', views.index_class, name='index_class'),
    path('func/', views.index_func, name='index_func'),
]