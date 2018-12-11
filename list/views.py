from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'list/index.html', {})
 
 
def detail(request, pk):
    pass
 
 
def create(request):
    pass
 
 
def update(request, pk):
    pass
 
 
def delete(request, pk):
    pass
    #return HttpResponse("Delete Post %s" % pk)
