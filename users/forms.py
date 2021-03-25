from django import forms
from .models import Users
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=32, label="사용자 이름", error_messages={
        'required': "아이디를 입력해주세요."
    })
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호", error_messages={
        'required': '비밀번호 입력해주세요. '
    })

    def clean(self):
        clean_data = super().clean()
        user_name = clean_data.get('user_name')
        password = clean_data.get('password')

        if user_name and password:
            user = Users.objects.get(user_name=user_name)
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.user_id = user.id
