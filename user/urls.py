# user_body_input_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.user, name='user'),
    # 다른 URL 패턴들
]