from django.db import models

# Create your models here.
# 장고에서 제공하는 Model을 상속받고
class Fcuser(models.Model):
    # username, password을 생성하고 길이 제한 두기 / verbose_nam 는 보여지는명
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    
    # email 추가
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자이메일')

    #dttm dateTimeField
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    
    # 내장함수 (1237.0.0에서 이름을 이제 username으로 볼수있음)
    def __str__(self):
        return self.username
    
    # 
    
    class Meta:
        # table명을 지정
        db_table = 'fastcampus_fcuesr'

        # 127.0.0.에 표시됨
        verbose_name = '패스트캠퍼스' # 패스트캠퍼스s
       # verbose_name_plural = '패스트 캠퍼스'
        

