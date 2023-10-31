from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:main')  # 회원가입 후 이동할 URL 설정
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')  # 로그인 후 이동할 URL 설정
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        logout(request)
    return redirect('main')  # 로그아웃 후 이동할 URL 설정