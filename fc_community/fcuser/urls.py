from django.urls import path
from . import views

urlpatterns = [
    # 순서 흐름
    # fc_community의 urls.py에서 
    # path('fcuser/', include('fcuser.urls')) 이 친구가 fcuser의 urls.py를 가리킴
    # fcuser의 urls에서 이제 register.html을 가리킴

    # 주소 :: http://127.0.0.1:8000/fcuser/register/ 
    path('register/', views.register),
    path('login/', views.login),
]
