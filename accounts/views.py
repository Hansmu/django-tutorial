from django.shortcuts import render
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords did not match!'})
    else:
        return render(request, 'accounts/signup.html')
