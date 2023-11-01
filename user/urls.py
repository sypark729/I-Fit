from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path("", views.user, name='user'),
    # 다른 URL 패턴들
]