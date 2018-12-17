from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'profile_image', 'profile_content', 'twitter')

    name = forms.TextInput(attrs={'size': 40})
    profile_image = forms.ImageField(required = False)
    profile_content = forms.Textarea(attrs={'cols': 20, 'rows': 2})
    twitter = forms.CharField(required=False)