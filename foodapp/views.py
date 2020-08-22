from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from . import forms


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
    template_name='foodapp/signup.html'

  
class TestPage(TemplateView):
    template_name='foodapp/home.html'


class ThanksPage(TemplateView):
    success_url=reverse_lazy('login')
    template_name='foodapp/thanks.html'
    








