from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == 'GET':
        form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('password2')

            if password == confirm_password:
                User.objects.create(username = username, password = password)
            else:
                print("password are not same")
        else:
            print("Form is not valid")
            
    return render(request, 'registration/register.html', {"form": form})
