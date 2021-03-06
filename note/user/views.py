from django.http import HttpResponse, HttpResponseRedirect
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
        # 检查登录状态，若登录，显示已登录
        # 检查session
        if request.session.get('name') and request.session.get('uid'):
            return HttpResponseRedirect('/home')

        # 检查cookies
        if request.COOKIES.get('name') and request.COOKIES.get('uid'):
            # 回写session
            request.session['name'] = request.COOKIES.get('name')
            request.session['uid'] = request.COOKIES.get('uid')
            return HttpResponseRedirect('/home')

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

        # 记录会话状态
        request.session['name'] = name
        request.session['uid'] = user.id

        # 是否勾选
        resp = HttpResponseRedirect('/home')
        if 'rememberMe' in request.POST:
            resp.set_cookie('name', name, max_age=3600 * 24 * 3)
            resp.set_cookie('uid', user.id, max_age=3600 * 24.3)

        return resp


def logout_view(request):
    # del session
    if 'name' in request.session:
        del request.session['name']
    if 'uid' in request.session:
        del request.session['uid']

    # del cookie
    resp = HttpResponseRedirect('/home')
    if 'name' in request.COOKIES:
        resp.delete_cookie('name')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')

    return resp
