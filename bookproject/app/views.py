from django.shortcuts import render


# Create your views here.
def book_list(request):
    book_list = {}
    return render(request, 'app/book_list.html', locals())
    # return render(request, 'app/book_list.html')


def index(request):
    return render(request, 'app/base.html')


def book_edit(request):
    return render(request, 'app/book_edit.html', locals())


def book_add(request):
    return render(request, 'app/book_add.html')


def author_list(request):
    return render(request, 'app/author_list.html')


def author_edit(request):
    return render(request, 'app/author_edit.html')


def author_add(request):
    return render(request, 'app/author_add.html')


def pub_list(request):
    return render(request, 'app/publisher_list.html')


def pub_edit(request):
    return render(request, 'app/publisher_edit.html')


def pub_add(request):
    return render(request, 'app/publisher_add.html')


def book_del(request):
    return None


def author_del(request):
    return None


def pub_del(request):
    return None