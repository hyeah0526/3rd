from django.shortcuts import render, redirect
from .models import Fcuser
# 비밀번호 암호화(make_password), 확인(check_password)
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .forms import LoginForm #form.py

# home
def home(request):
    user_id = request.session.get('user')

    if user_id : 
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home!')

# 로그인
def login(request) :
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form':form})



    # if request.method == 'GET' :
    #     return render(request, 'login.html')
    
    # elif request.method == 'POST' :
    #     # 받아온 값 확인
    #     username_input = request.POST.get('username', None)
    #     password_input = request.POST.get('password', None)
    #     print('username_input--> ', username_input)
    #     print('password_input--> ', password_input)

    #     # 값이 둘다 있는지 확인
    #     res_data = {}
    #     if not (username_input and password_input) :
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #         return render(request, 'login.html', res_data)
        
    #     else :
    #         # 아이디와 비밀번호가 일치하는지 확인
    #         # fcuser안의 objects안에 get이라는 함수를 사용
    #         # get안에 조건을 작성하여 사용자가 작성한 username이 있는지 확인 후 가져옴
    #         fcuser = Fcuser.objects.get(username=username_input)
    #         print('비밀번호 일치여부', check_password(password_input, fcuser.password))

    #         if check_password(password_input, fcuser.password):
    #             print('비밀번호 일치!')
    #             # 비밀번호가 맞으면 로그인 처리
    #             # return render(request, 'login.html')
    #             # 세션안에 있는 user에 사용자 아이디를 넣기
    #             request.session['user'] = fcuser.id

    #             # 로그인 -> 홈으로 이동 (리다이렉트)
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비멀번호가 틀렸습니다.'
    #         return render(request, 'login.html', res_data)



# 회원가입
def register(request) :

    if request.method == 'GET' :
        return render(request, 'register.html')
    

    elif request.method == 'POST' :
        # 값 받아오기
        # 예외처리 .get('', 기본값지정)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)

        # 비밀번호가 맞지않으면 에러 메세지와 함께 반환시키기
        # response시키기 위해서 import시켜주기 
        res_data = {}   # 에러메세지

        # 값이 하나라도 없으면 예외처리 해주기
        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다.'

        # 비밀번호와 비밀번호 확인이 다를 경우 예의처리
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        # 전부 들어있을 경우 저장
        else:
            # 클래스 import해주고 값 담아주기
            fcuser = Fcuser(
                username = username,
                password=make_password(password), # 비밀번호 암호화
                useremail = useremail
            )
            # 저장
            fcuser.save()

        # 확인 방법 : http://127.0.0.1:8000/admin/fcuser/fcuser/ 에서 제대로 저장됐는지 확인 가능

        return render(request, 'register.html', res_data)



