from django import forms
from django.core.exceptions import ValidationError

from arts.models import Arts


class AddArticleForm(forms.ModelForm):

    content = forms.CharField(label='content',
                              widget=forms.Textarea(attrs={
                                'class': 'content',
                                'cols': 30, 'rows': 10,
                                'maxlength': 256
                              }))
    image = forms.ImageField(label='image',
                             widget=forms.FileInput(attrs={
                                'class': 'inpt', 'type': 'file',
                                'accept': '.jpg, .jpeg, .png',
                                'multiple': True,
                                'id': 'image_uploads',
                             }))

    class Meta:

        model = Arts
        fields = ['title', 'slug', 'content', 'image', 'is_publish']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Length exceeds 100 characters')

        return title
