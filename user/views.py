# user/views.py
from django.shortcuts import render, redirect
from .forms import UserBodyInputForm
from .models import UserBodyInput


# 사용자 정보 입력 뷰
def user(request):
    if request.method == 'POST':
        form = UserBodyInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clothes')  # Clothes 앱의 URL 패턴명으로 변경
    else:
        form = UserBodyInputForm()
    return render(request, 'user/U_input.html', {'form': form})

