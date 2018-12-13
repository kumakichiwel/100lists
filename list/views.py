from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import ListForm
from .models import List

@login_required
def index(request):
    user_lists = List.objects.filter(user__id=request.user.id)
    return render(request, 'list/index.html', {'user_lists':user_lists})
 
 
def detail(request, pk):
    list_val = List.objects.get(id=pk)
    return render(request, 'list/detail.html', {'list_val':list_val})

 
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
                'image':list.image
            }
        )
        print("+++++++;")
        print(list.image_edit)
    return render(request, 'list/update.html', {'form':form, 'pk':pk, 'image_edit':list.image_edit})   

 
def delete(request, pk):
    List.objects.get(pk=pk).delete()
    return redirect('list:index')
    
