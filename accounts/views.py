from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm


@login_required
def index(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    if profile.exists():
        return render(request, 'accounts/index.html', {'profile':profile[0]})
    else:
        form = ProfileForm()
        return render(request, 'accounts/create_profile.html', {'form':form})


def detail(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    return render(request, 'accounts/detail.html', {'profile':profile})


@login_required
def create(request):
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user_id = request.user.id
        profile.save()
    return redirect('list:index')

@login_required
def update(request, pk):
    print("in 1")
    profile = get_object_or_404(Profile, id=pk)
    print("in 2")
    if request.method == "POST":
        print("in 3")
        form = ProfileForm(request.POST, request.FILES)
        print("in 4")
        if form.is_valid():
            print("in 5")
            print(form.cleaned_data['name'])
            profile.name = form.cleaned_data['name']
            print("in 5-1")
            print(form.cleaned_data['profile_image'])
            profile.profile_image = form.cleaned_data['profile_image']
            print("in 5-2")
            print(form.cleaned_data['profile_content'])
            profile.profile_content = form.cleaned_data['profile_content']
            print("in 5-3")
            print(form.cleaned_data['twitter'])
            profile.twitter = form.cleaned_data['twitter']
            print("in 6")
            print("+++++ profile +++++")
            print(profile)
            profile.save()
            print("in 7")
            return redirect('accounts:index')
    else:
        form = ProfileForm(
            initial={
                'name':profile.name,
                'profile_image':profile.profile_image,
                'profile_content':profile.profile_content,
                'twitter':profile.twitter,
            }
        )
    return render(request, 'accounts/update.html', {'form':form, 'pk':pk })   


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

