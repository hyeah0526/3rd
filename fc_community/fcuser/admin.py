from django.contrib import admin
from .models import Fcuser

class FcuserAdmin(admin.ModelAdmin):
    # 이렇게하면 127.0.0.1에서 사용자명과 비밀번호로 확인 가능함
    list_display = ('username', 'password', 'useremail')

admin.site.register(Fcuser, FcuserAdmin)


# 설정
