from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import RegistrationUserForm, LoginUserForm


def registration(request):
    if request.method == 'POST':
        form_regist = RegistrationUserForm(request.POST)
        form_login = LoginUserForm(request, data=request.POST)
        if form_regist.is_valid():
            user_new = form_regist.save()
            login(request, user_new)
            return redirect('home')
        elif form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            return redirect('home')

    form_regist = RegistrationUserForm()
    form_login = LoginUserForm()

    context = {
        'form_regist': form_regist,
        'form_login': form_login,
    }
    return render(request, 'users/registration.html', context=context)


def login_user(request):
    if request.method == 'POST':
        form_regist = RegistrationUserForm(request.POST)
        form_login = LoginUserForm(request, data=request.POST)
        if form_regist.is_valid():
            user_new = form_regist.save()
            login(request, user_new)
            return redirect('home')
        elif form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            return redirect('home')

    form_regist = RegistrationUserForm()
    form_login = LoginUserForm()

    context = {
        'form_regist': form_regist,
        'form_login': form_login,
    }
    return render(request, 'users/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')
