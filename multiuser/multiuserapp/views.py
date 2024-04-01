from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, DealerRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def user_home(request):
    return render(request, 'user_home.html')

def dealer_home(request):
    return render(request, 'dealer_home.html')

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def dealer_registration_view(request):
    if request.method == 'POST':
        form = DealerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dealer_home')  
    else:
        form = DealerRegistrationForm()
    return render(request, 'dealer_registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return HttpResponse('Error, user does not exist')
    else:
        return render(request, 'login.html')







# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         password = request.POST.get('pass')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')
#         else:
#             return HttpResponse('Error, user does not exist')
#     else:
#         return render(request, 'login.html')
