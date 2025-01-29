from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up_by_django, name='sign_up_by_django'),
    path('', views.sign_up_by_html, name='sign_up_by_html'),
]