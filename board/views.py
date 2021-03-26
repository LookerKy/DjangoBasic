from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from .forms import BoardForm
from users.models import Users
from tag.models import Tag
from django.core.paginator import Paginator


# Create your views here.
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, "board_detail.html", {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/users/login')
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)  # board와 관계를 맺고 있기 때문에 board를 먼저 생성해놓고 저장해야지 오류가 나지않음

            return redirect('/board/list')

    else:
        form = BoardForm()
        return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})
