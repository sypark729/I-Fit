from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('main/', views.main_page, name='main'),
]