from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome page'),
    path('p1/', views.show_options, name='show options'),
]