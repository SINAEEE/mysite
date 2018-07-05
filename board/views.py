from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board
from user.models import User



# Create your views here.

def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list' : board_list}
    return render(request, 'board/list.html', context)


def writeform(request):
    #인증 체크
    # if request.session['authuser'] is None:
    #     return HttpResponseRedirect('/user/loginform')
    # else:
        return render(request, 'board/writeform.html')


def write(request):
    #print(request.POST)
    #<QueryDict: {'csrfmiddlewaretoken': ['oaus3dlQyB6CvnTJuL4jMN1O13EfaCccMF9liEmiTqf3VXpxwmqJkD2gYhKXmqj3'], 'a': ['1'], 'title': ['1'], 'content': ['1']}>

    #board.user.id = request.session['authuser'][id]
    #print(request.POST['a'])

    board = Board()
    #board.user = User.objects.get(id=(request.POST.get('a'))[0])
    board.user = User.objects.get(id=request.POST['a'])
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()

    return HttpResponseRedirect('/board')


def view(request):
    #print(Board.objects.all())
    b_id = request.GET['b_id']
    #print(b_id)
    view_list = Board.objects.filter(id=b_id)
    #print(view_list) #<QuerySet [<Board: Board(1, 1, 0, 2018-07-04 13:45:56+00:00, 1)>]>
    #print(view_list[0]) #Board(1, 1, 0, 2018-07-04 13:45:56+00:00, 1)
    #print(model_to_dict(view_list[0])) #{'id': 1, 'title': '1', 'content': '1', 'hit': 0, 'user': 1}

    context = {'view_list' : view_list[0]}
    return render(request, 'board/view.html',context)


def delete(request):
    print(request.GET)
    b_id = request.GET['id']
    #print(b_id)
    Board.objects.filter(id=b_id).delete()
    #print(b_id)

    return HttpResponseRedirect('/board')
    #return render(request, 'board/list.html')


def modifyform(request):
    return render(request, 'board/modifyform.html')


def modify(request):
    pass




