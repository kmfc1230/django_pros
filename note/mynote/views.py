from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from mynote.models import Note


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'name' not in request.session or 'uid' not in request.session:
            # check cookie
            c_name = request.COOKIES.get('name')
            c_uid = request.COOKIES.get('uid')
            if not c_uid or not c_name:
                return HttpResponseRedirect('/home')
            else:
                request.session['name'] = c_name
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)

    return wrap


@check_login
def list_note(request):
    notes = Note.objects.filter(is_active=True)
    if request.method == 'GET':
        return render(request, 'mynote/list_note.html', locals())
    elif request.method == "POST":
        return HttpResponse('add note')


@check_login
def add_note(request):
    if request.method == 'GET':
        return render(request, 'mynote/add_note.html')
    elif request.method == 'POST':
        uid = request.session['uid']
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content, user_id=uid)

        return HttpResponseRedirect('/note/list_note')


@check_login
def update_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Exception as e:
        return HttpResponse('note not found %s' % e)
    if request.method == 'GET':
        title = note.title
        content = note.content
        return render(request, 'mynote/update_note.html', locals())

    return None


def delete_note(request, note_id):
    if not note_id:
        print('error')
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        return HttpResponse('note not found %s' % e)

    note.is_active = False
    note.save()
    return HttpResponseRedirect('/note/list_note/')


def restore(request):
    notes = Note.objects.all()
    for note in notes:
        note.is_active = True
        note.save()

    return HttpResponseRedirect('/note/list_note')