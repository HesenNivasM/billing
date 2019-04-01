from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login


def loginToSite(request):
    
    if request.method == "POST":
        print("hai")
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboardPanel')
            else:
                return render(request, 'login/loginToSite.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/loginToSite.html', {'error_message': 'Invalid Login. Please try again'})

    return render(request, 'login/loginToSite.html')