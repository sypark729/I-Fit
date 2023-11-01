from django.shortcuts import render, redirect
from .forms import UserBodyInputForm
from .models import UserBodyInput
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def user(request):
    # 사용자의 사이즈 정보가 있는지 확인
    try:
        user_body_input = request.user.userbodyinput
        # 기존 정보가 있는 경우, 수정을 위한 폼을 생성
        if request.method == 'POST':
            form = UserBodyInputForm(request.POST, instance=user_body_input)
            if form.is_valid():
                form.save()
                messages.success(request, '사이즈 정보가 수정되었습니다.')
                return redirect('clothes')
            else:
                messages.error(request, '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.')
        else:
            form = UserBodyInputForm(instance=user_body_input)
    except UserBodyInput.DoesNotExist:
        # 사용자의 사이즈 정보가 없는 경우, 새로운 정보를 입력하는 폼을 생성
        if request.method == 'POST':
            form = UserBodyInputForm(request.POST)
            if form.is_valid():
                user_body_input = form.save(commit=False)
                user_body_input.user = request.user
                user_body_input.save()
                messages.success(request, '사이즈 정보가 저장되었습니다.')
                return redirect('clothes')
            else:
                messages.error(request, '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.')
        else:
            form = UserBodyInputForm()
    
    return render(request, 'user/U_input.html', {'form': form})