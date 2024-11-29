from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    # 받아야하는 값 설정
    username = forms.CharField(max_length=32, label="사용자 이메일")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username_input = cleaned_data.get('username')
        password_input = cleaned_data.get('password')

        # 빈값일경우 
        if username_input and password_input:
            fcuser = Fcuser.objects.get(username = username_input)
            print('비밀번호 일치여부', check_password(password_input, fcuser.password))

            if not check_password(password_input, fcuser.password):
                print('비밀번호 유효성 검사 checkccc')
                self.add_error('password', '비밀번호를 틀렸습니다.')