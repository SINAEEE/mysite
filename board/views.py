from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board


# Create your views here.

def list(request):
        return render(request, 'board/list.html')
    # guestbook_list = Board.objects.all().order_by('-regdate')
    # context = {'guestbook_list': guestbook_list}
    # return render(request,'guestbook/list.html',context)


def writeform(request):
    #인증 체크
    # if request.session['authuser'] is None:
    #     return HttpResponseRedirect('/user/loginform')
    # else:
        return render(request, 'board/writeform.html')

def write(request):

    Board.title = request.POST['title']
    Board.content = request.POST['content']

    Board.save()

    return HttpResponseRedirect('/board')




