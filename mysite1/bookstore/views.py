from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from bookstore.models import Book


def index(request):
    return None


def all_book(request):
    all_book = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        return HttpResponse('--The book is not existed')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        # 查
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        # 改
        book.price = price
        book.market_price = market_price
        # 存
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    book_id = request.GET.get('book_id')
    if not book_id:
        print('---请求异常')
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('---delete_book err %s' % e)
        return HttpResponse('---the book is error')
    book.is_active = False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')
