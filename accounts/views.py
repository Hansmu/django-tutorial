from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'User has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                login(request, user)

            return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords did not match!'})
    else:
        return render(request, 'accounts/signup.html')
