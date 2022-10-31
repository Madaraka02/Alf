from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login



# Create your views here.
def register(request):
    form = CustomUserCreatinForm()
    if request.method == 'POST':
        form = CustomUserCreatinForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('home')

    return render(request, 'registration/registration.html', {'form':form})        

def update_profile(request,id):
    profile=get_object_or_404(Profile, id=id)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)

        if form.is_valid():
            form.save()

    return render(request, 'form.html', {'form':form})    


def profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)

    context={
        'profile':profile
    }
    return render(request, 'admin-profile.html', context)