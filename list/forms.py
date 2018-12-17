from django import forms
from django.forms import ModelForm
from .models import List, Comment


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('title', 'content', 'due_date', 'rank', 'image', 'share')

    '''
    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['origin'].widget.attrs = {'id':'selectedFile'} 
    '''
    choice_list_rank = (
        (1, u'A（最優先でやる）'),
        (2, u'B（そのうちやる）'),
        (3, u'C（いつかやる）'),
    )

    choice_list_share = (
        (1, u'公開する'),
        (2, u'公開しない'),
    )

    title = forms.TextInput(attrs={'placeholder': 'Enter description here', 'size': 40})
    content = forms.Textarea(attrs={'cols': 20, 'rows': 2})
    due_date = forms.DateTimeField(required=False)
    rank = forms.ChoiceField(choices=choice_list_rank, initial=1)
    image = forms.ImageField(required = False)
    share = forms.ChoiceField(choices=choice_list_share, initial=2)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

    comment = forms.Textarea(),
