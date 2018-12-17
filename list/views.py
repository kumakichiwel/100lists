from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import ListForm, CommentForm
from .models import List, Comment


@login_required
def index(request):
    user_lists = List.objects.filter(user__id=request.user.id)
    return render(request, 'list/index.html', {'user_lists':user_lists})
 
 
def detail(request, pk):
    list_val = List.objects.get(id=pk)
    comment_val = Comment.objects.filter(list_id=pk)
    form = CommentForm()
    return render(request, 'list/detail.html', {'list_val':list_val, 'comment_val':comment_val, 'form':form })

 
def create(request):
    if request.method == "POST":
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            List = form.save(commit=False)
            List.user_id = request.user.id
            List.save()
            return redirect('list:index')
    else:
        form = ListForm()
    return render(request, 'list/create.html', {'form':form})
 
 
def update(request, pk):
    list = get_object_or_404(List, id=pk)

    if request.method == "POST":
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            list.title = form.cleaned_data['title']
            list.content = form.cleaned_data['content']
            list.due_date = form.cleaned_data['due_date']
            list.rank = form.cleaned_data['rank']
            list.share = form.cleaned_data['share']
            list.image = form.cleaned_data['image']
            list.save()
            return redirect('list:index')
    else:
        form = ListForm(
            initial={
                'title':list.title,
                'content':list.content,
                'due_date':list.due_date,
                'rank':list.rank,
                'share':list.share,
                'image':list.image
            }
        )
    return render(request, 'list/update.html', {'form':form, 'pk':pk, 'image_edit':list.image_edit})   

 
def delete(request, pk):
    List.objects.get(pk=pk).delete()
    return redirect('list:index')


def create_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        Comment = form.save(commit=False)
        Comment.list_id = pk
        Comment.save()
    return redirect('list:detail', pk=pk)


def delete_comment(request, pk, id):
    Comment.objects.get(pk=pk).delete()
    return redirect('list:detail', pk=id)


def status_update(request, pk):
    list = get_object_or_404(List, id=pk)
    if list.status == False:
        list.status = True
    else:
        list.status = False
    list.save()
    return redirect('list:index')


def others_list(request):
    lists = List.objects.filter(share=1).exclude(user_id=request.user.id).order_by('created_at')[:10]
    return render(request, 'list/others.html', {'lists':lists})

