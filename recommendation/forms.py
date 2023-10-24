from django import forms

class SizeRecommendationForm(forms.Form):
    GENDER_CHOICES = [
        ('male', '남성'),
        ('female', '여성'),
    ]

    CLOTHING_CHOICES = [
        ('outer', '아우터'),
        ('top', '상의'),
        ('bottom', '바지'),
        ('skirt', '치마'),
    ]

    gender = forms.ChoiceField(label='성별', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    height = forms.DecimalField(label='키 (cm)', min_value=0)
    weight = forms.DecimalField(label='몸무게 (kg)', min_value=0)
    clothing_type = forms.ChoiceField(label='옷의 종류', choices=CLOTHING_CHOICES, widget=forms.RadioSelect)

    # 다양한 옷 치수 필드 정의
    # 아우터와 상의의 경우
    shoulder = forms.DecimalField(label='어깨너비 (cm)', min_value=0)
    chest = forms.DecimalField(label='가슴단면 (cm)', min_value=0)
    total_length = forms.DecimalField(label='총장 (cm)', min_value=0)
    sleeve = forms.DecimalField(label='소매길이 (cm)', min_value=0)

    # 바지와 치마의 경우
    waist = forms.DecimalField(label='허리둘레 (cm)', min_value=0)
    hip = forms.DecimalField(label='엉덩이둘레 (cm)', min_value=0)
    bottom_length = forms.DecimalField(label='밑단둘레 (cm)', min_value=0)
    thigh = forms.DecimalField(label='허벅지둘레 (cm)', min_value=0)