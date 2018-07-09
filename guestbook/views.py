
from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook

# Create your views here.


def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate') #object : DB Table 행
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
    a_id = request.GET['id']
    context = {'a_id': a_id}
    return render(request, 'guestbook/deleteform.html',context)

def delete(request):
    #guestbook = Guestbook()
    #print(request.POST)
    #print(request.POST['no'])
    Guestbook.objects.filter(id=request.POST['no']).filter(password=request.POST['password']).delete()

    return HttpResponseRedirect('/guestbook')




