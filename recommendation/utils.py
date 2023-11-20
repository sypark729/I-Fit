def recommend_size(request):
    size_keys = [
        ('shoulder', 'recommended_size_shoulder'),
        ('chest', 'recommended_size_chest'),
        ('total_length', 'recommended_size_total_length'),
        ('sleeve', 'recommended_size_sleeve'),
        ('neck', 'recommended_size_neck'),
        ('ntk', 'recommended_size_ntk'),
        ('waist', 'recommended_size_waist'),
        ('hip', 'recommended_size_hip'),
        ('bottom_length', 'recommended_size_bottom_length'),
        ('thigh', 'recommended_size_thigh'),
    ]
    recommended_sizes = {key: request.session.get(value, 0) for key, value in size_keys}
    return recommended_sizes

def diff(request):
    # 예측된 사용자 신체 사이즈 가져오기
    predicted_sizes = {
        'shoulder': round(request.session.get('predict_shoulder', 0), 2),
        'chest': round(request.session.get('predict_chest', 0), 2),
        'total_length': round(request.session.get('predict_top', 0), 2),
        'sleeve': round(request.session.get('predict_arm', 0), 2),
        'ntk' : round(request.session.get('predict_ntk', 0), 2) ,
        'neck' : round(request.session.get('predict_neck', 0), 2) ,
        'waist': round(request.session.get('predict_waist', 0), 2),
        'hip': round(request.session.get('predict_ass', 0), 2),
        'bottom_length': round(request.session.get('predict_bottom', 0), 2),
        'thighs': round(request.session.get('predict_thighs', 0), 2),
        }
    
    # 입력된 옷 사이즈 가져오기
    clothing_type = request.session.get('clothing_type')
    clothes_sizes = {
        'shoulder': round(request.session.get('shoulder', 0), 2),
        'chest': round(request.session.get('chest', 0), 2),
        'ntk': round(request.session.get('ntk', 0), 2),
        'total_length': round(request.session.get('total_length', 0), 2),
        'neck': round(request.session.get('neck', 0), 2),
        'sleeve': round(request.session.get('sleeve', 0), 2),
        'waist': round(request.session.get('waist', 0), 2),
        'hip': round(request.session.get('hip', 0), 2),
        'bottom_length': round(request.session.get('bottom_length', 0), 2),
        'thighs': round(request.session.get('thighs', 0), 2),
    }

    # 차이 계산 및 세션에 저장    
    differences = {}
    for size_name, predicted_size in predicted_sizes.items():
        clothes_size = clothes_sizes.get(size_name, 0)
        difference = predicted_size - clothes_size
        comparison = '작습니다' if difference > 0 else '큽니다' if difference < 0 else '같습니다'
        differences[size_name] = {
            'difference': round(abs(difference), 2),
            'comparison': comparison
        }
        request.session[f'diff_{size_name}'] = differences[size_name]

        if comparison == '작습니다':
            request.session['size_message'] = '옷이 작습니다. 큰 사이즈의 옷을 비교해 보세요.'
            break  # 하나라도 작은 경우 메시지 표시 후 종료
        elif comparison == '큽니다':
            request.session['size_message'] = '옷이 큽니다.'
        else:
            # 모든 사이즈가 같거나 큰 경우의 메시지
            request.session['size_message'] = '옷 사이즈가 적절합니다.'

    return differences
