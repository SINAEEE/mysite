from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request,'guestbook/list.html',context)

def writeform(request):
    #인증 체크
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')
