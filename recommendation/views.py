from django.shortcuts import render, redirect
from .utils import recommend_size, diff

def recommendation(request):
        size_differences = diff(request)

        predicted_sizes = {
            'shoulder': request.session.get('predict_shoulder', 0),
            'chest': request.session.get('predict_chest', 0),
            'total_length': request.session.get('predict_top', 0),
            'sleeve': request.session.get('predict_arm', 0),
            'waist': request.session.get('predict_waist', 0),
            'hip': request.session.get('predict_ass', 0),
            'bottom_length': request.session.get('predict_bottom', 0),
            'thighs': request.session.get('predict_thighs', 0),
        }

        clothes_sizes = {
            'shoulder': request.session.get('shoulder', 0),
            'chest': request.session.get('chest', 0),
            'total_length': request.session.get('total_length', 0),
            'sleeve': request.session.get('sleeve', 0),
            'waist': request.session.get('waist', 0),
            'hip': request.session.get('hip', 0),
            'bottom_length': request.session.get('bottom_length', 0),
            'thighs': request.session.get('thigh', 0),
    }
        for size_name, predicted_size in predicted_sizes.items():
            print(f"Predicted {size_name}: {predicted_size}")

        for size_name, clothes_size in clothes_sizes.items():
            print(f"Clothes {size_name}: {clothes_size}")


        # 추천 사이즈 계산
        recommended_sizes = recommend_size(request)

        formatted_shoulder = "{:.2f}".format(float(recommended_sizes.get('recommended_size_shoulder', 0)))
        formatted_chest = "{:.2f}".format(float(recommended_sizes.get('recommended_size_chest', 0)))
        formatted_total_length = "{:.2f}".format(float(recommended_sizes.get('recommended_size_total_length', 0)))
        formatted_sleeve = "{:.2f}".format(float(recommended_sizes.get('recommended_size_sleeve', 0)))
        formatted_waist = "{:.2f}".format(float(recommended_sizes.get('recommended_size_waist', 0)))
        formatted_hip = "{:.2f}".format(float(recommended_sizes.get('recommended_size_hip', 0)))
        formatted_bottom_length = "{:.2f}".format(float(recommended_sizes.get('recommended_size_bottom_length', 0)))
        formatted_thigh = "{:.2f}".format(float(recommended_sizes.get('recommended_size_thigh', 0)))

        result_data = {
            'recommended_size_shoulder': formatted_shoulder,
            'recommended_size_chest': formatted_chest,
            'recommended_size_total_length': formatted_total_length,
            'recommended_size_sleeve': formatted_sleeve,
            'recommended_size_waist': formatted_waist,
            'recommended_size_hip': formatted_hip,
            'recommended_size_bottom_length': formatted_bottom_length,
            'recommended_size_thigh': formatted_thigh,
            'size_differences': size_differences,
            'recommended_sizes': recommended_sizes,
            'predicted_sizes': predicted_sizes,
        }

        print("Result Data:", result_data)  # 중간 결과 확인

        return render(request, 'recommendation/result.html', result_data)