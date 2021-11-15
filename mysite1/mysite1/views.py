from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def birthday(request, y, m, d):
    return HttpResponse("birthday: %s/%s/%s" % (y, m, d))


def page_n(request, page):
    return HttpResponse("<h1>This is Page %d</h1>" % page)


def test_html(request):
    # 方法一
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)

    # 方法二
    dic = {
        'username': 'haisheng',
        'age': '18',
    }
    return render(request, 'test_html.html', dic)


def index(request):
    return HttpResponse("index")


def test_html_param(request):
    dic = {}
    dic['int'] = 88
    dic['str'] = 'haisheng'
    dic['list'] = ["tom", "jack", "lucy"]
    dic['dict'] = {'a': 9, 'b': 8, 'c': 6}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()

    return render(request, 'test_html_param.html', dic)


def say_hi():
    return "hahaha"


class Dog():
    def say(self):
        return "wangwang"


def test_if_for(request):
    dic = {}
    dic['a'] = 10
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == "POST":
        # 处理计算
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        result = 0
        if op == "add":
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        elif op == "div":
            result = x / y
        return render(request, 'mycal.html', locals())


def test_static(request):
    return render(request, 'test_static.html')
