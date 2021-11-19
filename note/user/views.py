from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User
import hashlib


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        pwd_1 = request.POST.get('pwd_1')
        pwd_2 = request.POST.get('pwd_2')

        user = User.objects.filter(name=name)
        if user:
            print('user exists')
            return HttpResponse('user exists')
        if pwd_1 != pwd_2:
            print('两次密码不一致')
            return HttpResponse('两次密码不一致')

        m = hashlib.md5()
        m.update(pwd_1.encode())
        pwd = m.hexdigest()
        User.objects.create(name=name, pwd=pwd)
        return HttpResponse('注册成功')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')

        if not name or not pwd:
            return HttpResponse('用户名或密码不能为空')

        user = ''
        try:
            user = User.objects.get(name=name)
        except Exception as e:
            print("--%s--" % e)
            return HttpResponse('用户名或密码有误')

        m = hashlib.md5()
        m.update(pwd.encode())
        pwd_m = m.hexdigest()
        if pwd_m != user.pwd:
            return HttpResponse('用户名或密码有误')

        return HttpResponse('登录成功')
