from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from user.forms import SignUp, SignIn


def register_view(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('control_panel')

    ctx = {
        'form': form,
    }
    return render(request,'user/register.html',context=ctx)


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return redirect('control_panel')
        else:
            return redirect('menu')
    form = SignIn()
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if request.user.is_staff or request.user.is_superuser:
                    return redirect('control_panel')
                else:
                    return redirect('menu')
    ctx = {
        'form': form,
    }
    return render(request,'user/login.html',context=ctx)




def logout_view(request):
    logout(request)
    return redirect('login_page')