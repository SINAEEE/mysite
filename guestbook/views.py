
from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook

# Create your views here.


def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request,'guestbook/list.html',context)


def add(request):
    guestbook = Guestbook()

    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.message = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    return render(request, 'guestbook/deleteform.html')


def delete(request):
    guestbook = Guestbook()
    guestbook.objects.filter(id=request.POST.get('id','')).filter(password=request.POST.get('password','')).delete()

    guestbook.save()

    return HttpResponseRedirect('/guestbook')




