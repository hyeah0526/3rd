from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password # 비밀번호 암호화
from django.http import HttpResponse 

def register(request) :

    if request.method == 'GET' :
        return render(request, 'register.html')
    

    elif request.method == 'POST' :
        # 값 받아오기
        # 예외처리 .get('', 기본값지정)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # 비밀번호가 맞지않으면 에러 메세지와 함께 반환시키기
        # response시키기 위해서 import시켜주기 
        res_data = {}   # 에러메세지

        # 값이 하나라도 없으면 예외처리 해주기
        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'

        # 비밀번호와 비밀번호 확인이 다를 경우 예의처리
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        # 전부 들어있을 경우 저장
        else:
            # 클래스 import해주고 값 담아주기
            fcuser = Fcuser(
                username = username,
                password=make_password(password) # 비밀번호 암호화
            )
            # 저장
            fcuser.save()

        # 확인 방법 : http://127.0.0.1:8000/admin/fcuser/fcuser/ 에서 제대로 저장됐는지 확인 가능

        return render(request, 'register.html', res_data)



