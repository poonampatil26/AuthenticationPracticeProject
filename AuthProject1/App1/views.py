from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def loginView(request):
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        print(u,p)
        user = authenticate(username=u, password=p)

        if user is not None:
            print('valid credential')
            print('Login code')
            login(request, user)
            return redirect('result')
        else:
            print('Invalid credential')
            messages.error(request,'Invalid credentials')

    template_name = 'App1/login.html'
    context ={}
    return render(request, template_name, context)


def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    template_name = 'App1/register.html'
    context = {'form':form}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')


def home(request):
    template_name = 'App1/home.html'
    context = {}
    return render(request, template_name, context)

def result(request):
    template_name = 'App1/result.html'
    context = {}
    return render(request, template_name, context)