from django.shortcuts import render, redirect
from .forms import SizeRecommendationForm
from .utils import recommend_size
from django.http import HttpResponse  # HttpResponse 추가

def recommendation(request):
    if request.method == 'POST':
        # form을 직접 생성하지 않고, POST 데이터를 사용하지 않는다.
        # form = SizeRecommendationForm(request.POST)

        # POST 데이터에서 필요한 값을 직접 추출
        predict_top = request.session.get('predict_top', 0)
        predict_chest = request.session.get('predict_chest', 0)
        predict_shoulder = request.session.get('predict_shoulder', 0)
        predict_arm = request.session.get('predict_arm', 0)
        predict_waist = request.session.get('predict_waist', 0)
        predict_ass = request.session.get('predict_ass', 0)
        predict_bottom = request.session.get('predict_bottom', 0)
        predict_thighs = request.session.get('predict_thighs', 0)
        clothing_type = request.session.get('clothing_type')

        # 예측한 사용자 신체 치수 정보
        print(f"predict_top: {predict_top}")

        # 상의
        if clothing_type in ['outer', 'top']:
            clothes_shoulder = request.session.get('clothes_shoulder', 0)
            clothes_chest = request.session.get('clothes_chest', 0)
            clothes_total_length = request.session.get('clothes_total_length', 0)
            clothes_sleeve = request.session.get('clothes_sleeve', 0)

            diff_shoulder = abs(predict_shoulder - clothes_shoulder)
            diff_chest = abs(predict_chest - clothes_chest)
            diff_total_length = abs(predict_top - clothes_total_length)
            diff_sleeve = abs(predict_arm - clothes_sleeve)

            request.session['diff_shoulder'] = diff_shoulder
            request.session['diff_chest'] = diff_chest
            request.session['diff_total_length'] = diff_total_length
            request.session['diff_sleeve'] = diff_sleeve

        # 하의
        elif clothing_type in ['bottom', 'skirt']:
            clothes_waist = request.session.get('clothes_waist', 0)
            clothes_hip = request.session.get('clothes_hip', 0)
            clothes_bottom_length = request.session.get('clothes_bottom_length', 0)
            clothes_thigh = request.session.get('clothes_thigh', 0)

            diff_waist = abs(predict_waist - clothes_waist)
            diff_hip = abs(predict_ass - clothes_hip)
            diff_bottom_length = abs(predict_bottom - clothes_bottom_length)
            diff_thigh = abs(predict_thighs - clothes_thigh)

            request.session['diff_waist'] = diff_waist
            request.session['diff_hip'] = diff_hip
            request.session['diff_bottom_length'] = diff_bottom_length
            request.session['diff_thigh'] = diff_thigh

        print(f"Session data: {request.session}")

        # 추천 함수 호출 위치 수정
        result_data = recommend_size(request)
        print(f"Session data after recommend_size: {request.session}")
        print(result_data)

        result_data.update({
            'diff_shoulder': request.session.get('diff_shoulder'),
            'diff_chest': request.session.get('diff_chest'),
            'diff_total_length': request.session.get('diff_total_length'),
            'diff_sleeve': request.session.get('diff_sleeve'),
            'diff_waist': request.session.get('diff_waist'),
            'diff_hip': request.session.get('diff_hip'),
            'diff_bottom_length': request.session.get('diff_bottom_length'),
            'diff_thigh': request.session.get('diff_thigh'),
        })

        return render(request, 'recommendation/result.html', result_data)

    else:
        # 폼을 생성하는 부분 생략
        # form = SizeRecommendationForm()

        # 폼이 필요하지 않은 경우 바로 결과값을 보여줌
        return render(request, 'recommendation/result.html', {'form': None})