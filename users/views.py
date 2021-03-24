from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import Users


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        body = request.POST
        user_name = body.get('username', None)
        password = body.get('password', None)

        res_data = {}

        if not (user_name and password):
            res_data['error'] = "모든값을 입력해야됩니다."
        else:
            user = Users.objects.get(user_name=user_name)
            if check_password(password, user.password):
                # 로그인 처리
                pass
            else:
                res_data['error'] = "모든값을 입력해야됩니다."

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        body = request.POST
        username = body.get('username', None)
        email = body.get('email', None)
        password = body.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and password and re_password and email):
            res_data['error'] = '모든 값을 입력해야합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            users = Users(user_name=username, email=email, password=make_password(password))
            users.save()

        return render(request, 'register.html', res_data)
