import password as password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from user.models import User
import hashlib


def register_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if not username or not password_1 or not password_2:
            return HttpResponse('用户名和密码不能为空')

        users = User.objects.filter(username=username)
        if users:
            return HttpResponse('用户已注册')

        if password_1 != password_2:
            return HttpResponse('两次密码不一致')

        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        User.objects.create(username=username, password=password_m)

        print('username: %s\npassword: %s ' % (username, password_m))
        return HttpResponse('注册成功')


def login_view(request):
    if request.method == 'GET':
        # 检查session和COOKIES
        if request.session.get('userid') and request.session.get('username'):
            return HttpResponseRedirect('/')
        c_username = request.COOKIES.get('username')
        c_userid = request.COOKIES.get('userid')
        if c_userid and c_username:
            request.session['username'] = c_username
            request.session['userid'] = c_userid
            return HttpResponseRedirect('/')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        if not username or not password:
            return HttpResponse('用户名和密码不能为空')

        m = hashlib.md5()
        m.update(pwd.encode())
        password_m = m.hexdigest()
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('%s' % e)

        if user.password != password_m:
            return HttpResponse('用户名或密码错误')

        # 记录会话状态
        request.session['username'] = username
        request.session['userid'] = user.id

        resp = HttpResponseRedirect('/')
        print(request.POST)
        if 'remeberMe' in request.POST:
            '''
            中文不能通过‘latin-1’编码
            解决方案：
            1、设置cookie
            newuser = username.encode('utf-8').decode('latin-1')
            response.set_cookie('uname',newuser) 
            2、获取cookie
            if request.COOKIES.get('uname'):
                context['uname'] = request.COOKIES['uname'].encode('latin-1').decode('utf-8')
            '''
            resp.set_cookie('username', username.encode('utf-8').decode('latin-1'), max_age=3600 * 24 * 3)
            resp.set_cookie('userid', user.id, max_age=3600 * 24 * 3)

        return resp


def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    if 'userid' in request.session:
        del request.session['userid']

    resp = HttpResponseRedirect('/')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'userid' in request.COOKIES:
        resp.delete_cookie('userid')

    return resp
