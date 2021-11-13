from django.http import HttpResponse


def birthday(request, y, m, d):
    return HttpResponse("birthday: %s/%s/%s" % (y, m, d))


def page_n(request, page):
    return HttpResponse("<h1>This is Page %d</h1>" % page)
