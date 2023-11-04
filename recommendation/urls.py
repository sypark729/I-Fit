from django.urls import path
from . import views

app_name = 'recommendation'  # 앱의 이름을 정의합니다.

urlpatterns = [
    path("", views.recommendation, name='recommendation'),
]