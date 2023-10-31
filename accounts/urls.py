from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'  # 앱의 이름을 정의합니다.

urlpatterns = [
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]