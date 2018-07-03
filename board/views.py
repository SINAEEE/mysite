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
    b_id = request.GET['id']
    print(b_id)
    if Board.objects.filter(id=b_id):
    view_list = Board.objects.get(id=b_id)
    print(view_list)


    return render(request, 'board/view.html')



