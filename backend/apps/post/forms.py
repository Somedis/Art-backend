from django import forms

from .models import Posts


class PostForm(forms.ModelForm):

    content = forms.CharField(label='content',
                              widget=forms.Textarea(attrs={
                                'class': 'content',
                                'cols': 30, 'rows': 10,
                                'maxlength': 256
                              }))

    class Meta:
        model = Posts
        fields = ['title', 'content']
