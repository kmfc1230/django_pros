from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User
import hashlib


def index(request):
    return HttpResponse('index')


def reg_view(request):
    # 注册
    if request.method == 'GET':
        #  GET 返回页面
        return render(request, 'user/register.html')
    #  POST 处理提交数据
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        #   1.当前用户名是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')

        if len(username) > 30:
            return HttpResponse('用户名过长')

        #   2.两次密码要保持一致
        if password_1 != password_2:
            return HttpResponse('两次密码不一致')

        #   3.插入数据[暂时先明文处理]
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            # 有可能报错，重复插入[唯一索引并发写入问题]
            print('--create user error: %s' % e)
            return HttpResponse('用户名已注册')

        # 免一天登录
        request.session['username'] = username
        request.session['uid'] = user.id
        # TODO 修改session存储时间为1天

        return HttpResponse('注册成功')


def login_view(request):
    user = ''
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login error: %s' % e)
            return HttpResponse('用户名或密码错误')

        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误')

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        resp = HttpResponse('%s登录成功' % user.username)

        # 判断是否勾选了‘记住用户名’
        # 勾了存cookie 存储username.uid 时间3天
        if 'checkbox' in request.POST:
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)

        return resp
