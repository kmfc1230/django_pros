import content as content
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from note.models import Note
from user.models import User


def check_login(fn):
    def wrapper(request, *args, **kwargs):
        # check session
        if 'username' not in request.session or 'userid' not in request.session:
            # check cookie
            c_username = request.COOKIES.get('username')
            c_userid = request.COOKIES.get('userid')
            if not c_userid or c_username:
                return HttpResponseRedirect('/')
            else:
                request.session['username'] = c_username
                request.session['userid'] = c_userid

        return fn(request, *args, **kwargs)

    return wrapper


@check_login
def list_note(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.session.get('username'))
        notes = Note.objects.filter(is_active=True).filter(user=user)
        return render(request, 'note/list_note.html', locals())
    elif request.method == 'POST':
        return HttpResponse('note list')


@check_login
def add_note(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = User.objects.get(username=request.session.get('username'))
        Note.objects.create(title=title, content=content, user=user)
        return HttpResponseRedirect('/note/list')


@check_login
def del_note(request, id):
    note = Note.objects.get(id=id)
    note.is_active = False
    note.save()
    return HttpResponseRedirect('/note/list')


@check_login
def update_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'note/update.html', {'note': note})
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/list')

    return


@check_login
def restore(request):
    notes = Note.objects.all()
    for note in notes:
        note.is_active = True
        note.save()
    return HttpResponseRedirect('/note/list')
