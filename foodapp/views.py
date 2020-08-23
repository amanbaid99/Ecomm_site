from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import forms
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView



# Create your views here.

def home(request):
   
    return render(request,"foodapp/home.html")

def store(request):
    
    return render(request,"foodapp/store.html")

def cart(request):

    return render(request,"foodapp/cart.html")

def checkout(request):

    return render(request,"foodapp/checkout.html")


class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class LogOutView(TemplateView):
    template_name = "foodapp/login.html"

class LogInView(TemplateView):
    template_name = "foodapp/home.html"



# class SignUp(CreateView):
#     form_class=forms.UserCreateForm
#     success_url=reverse_lazy('login')
#     template_name='foodapp/signup.html'

  
# class TestPage(TemplateView):
#     template_name='foodapp/home.html'


# class ThanksPage(TemplateView):
#     success_url=reverse_lazy('login')
#     template_name='foodapp/thanks.html'
    








