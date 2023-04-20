from django import forms
from django.core.exceptions import ValidationError

from arts.models import Arts


class AddArticleForm(forms.ModelForm):

    image = forms.ImageField(label='image',
                             widget=forms.FileInput(attrs={
                                'class': 'inpt', 'type': 'file',
                                'accept': '.jpg, .jpeg, .png',
                                'multiple': True,
                                'id': 'image_uploads',
                             }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'not selected'

    class Meta:

        model = Arts
        fields = ['title', 'slug', 'image', 'is_publish', 'cat']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Length exceeds 100 characters')

        return title
