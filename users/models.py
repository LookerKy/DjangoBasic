from django.db import models


# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=64, verbose_name="사용자명")
    email = models.EmailField(max_length=128, verbose_name="이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_date_time = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    # 클래스가 문자열로 변경될 때 어떻게 반환할지 설정 할 수 있는 내장함수
    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'board_users'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
