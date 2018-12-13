from django import forms
from django.forms import ModelForm
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('title', 'content', 'due_date', 'rank', 'image')

    '''
    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['origin'].widget.attrs = {'id':'selectedFile'} 
    '''
    choice_list = (
        (1, u'A（最優先でやる）'),
        (2, u'B（そのうちやる）'),
        (3, u'C（いつかやる）'),
    )

    title = forms.TextInput(attrs={'placeholder': 'Enter description here', 'size': 40}),
    content = forms.Textarea(attrs={'cols': 20, 'rows': 2}),
    due_date = forms.DateTimeField(),
    rank = forms.ChoiceField(choices=choice_list, initial=1)
    image = forms.ImageField(required = False)
