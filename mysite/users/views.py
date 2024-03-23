from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    
    return render(request, 'users/register.html',{'form':form})

@login_required
def profilePage(request):
    return render(request,'users/profile.html')

