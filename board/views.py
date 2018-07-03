from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board



# Create your views here.

def list(request):
    board_list = Board.objects.all()
    context = {'board_list' : board_list}
    return render(request, 'board/list.html', context)
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
    #print(request.POST[0])
    #r1 = request.POST[0]
    board = Board()
    #request.session['r1'] = model_to_dict(r1)
    #print(r1)
    #board.user.id = request.session['authuser'][id]
    board.user.id = request.POST[0]['id']
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()

    return HttpResponseRedirect('/board')




