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


def create(request):
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        List = form.save(commit=False)
        List.user_id = request.user.id
        List.save()
    return redirect('list:index')


def update(request, pk):
    profile = get_object_or_404(Profile, id=pk)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.name = form.cleaned_data['name']
            profile.profile_image = form.cleaned_data['profile_image']
            profile.profile_content = form.cleaned_data['profile_content']
            profile.save()
            return redirect('accounts:index')
    else:
        form = ProfileForm(
            initial={
                'name':profile.name,
                'profile_image':profile.profile_image,
                'profile_content':profile.profile_content,
            }
        )
    return render(request, 'accounts/update.html', {'form':form, 'pk':pk })   


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
