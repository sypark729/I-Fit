# user_body_input_app/views.py
from django.shortcuts import render, redirect
from .forms import UserBodyInputForm
from .models import UserBodyInput

# Create your views here.

def user(request):
    if request.method == 'POST':
        form = UserBodyInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recommendation')  # 추천 화면으로 이동
    else:
        form = UserBodyInputForm()
    return render(request, 'user/U_input.html', {'form': form})