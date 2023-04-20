from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationUserForm(UserCreationForm):

    username = forms.CharField(label='username', required=True,
                               widget=forms.TextInput(
                                    attrs={'autocomplete': 'off'})
                               )
    email = forms.EmailField(label='email', required=True,
                             widget=forms.EmailInput(
                                attrs={'autocomplete': 'off'})
                             )
    password1 = forms.CharField(label='password', required=True,
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'off'})
                                )
    password2 = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='username',
                               widget=forms.TextInput(
                                    attrs={'autocomplete': 'off'})
                               )
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'off'})
                               )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['id'] = 'logusername'

    class Meta:
        model = User
        fields = ('username', 'password')
