from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import RegistrationUserForm, LoginUserForm


class RegistrationUser(CreateView):

    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
