from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView,logout_then_login
from django.urls import reverse_lazy,reverse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
class userloginview(LoginView):
    template_name ='login.html'
    success_url = reverse_lazy('home')

class userlogoutview(LogoutView):
    template_name ='login.html'
    success_url = reverse_lazy('login')


def logout(request):
    return logout_then_login(request, login_url=reverse('login'))


def register(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            # messages.success(request,"Registration successful.")
            return HttpResponseRedirect(reverse('home'))

    form=NewUserForm()
    return render(request,template_name='register.html',context={'form':form})
