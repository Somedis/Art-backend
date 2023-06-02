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
                                attrs={'autocomplete': 'off',
                                       'onchange': 'checkValid();',
                                       'class': 'formlab'})
                             )
    password1 = forms.CharField(label='password', required=True,
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'off'})
                                )
    password2 = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.exclude(pk=self.instance.pk).filter(username=username)\
                .exists():
            raise forms.ValidationError('Username is already exist')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.exclude(pk=self.instance.pk).filter(email=email)\
                .exists():
            raise forms.ValidationError('Email is already exist')
        return email

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

    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password."
        ),
        "inactive": ("This account is inactive."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['id'] = 'logusername'

    def clean_username(self):
        return self.cleaned_data['username'].lower()

    class Meta:
        model = User
        fields = ('username', 'password')
