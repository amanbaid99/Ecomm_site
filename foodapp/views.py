from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import forms
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
import json



# Create your views here.

def home(request):
    businesses= Business.objects.all()
    context={'businesses':businesses}
   
    return render(request,"foodapp/home.html",context)

def store(request,id):
    menus=Menu.objects.filter(business_id=id)
    context={'menus':menus}
    return render(request,"foodapp/store.html",context)

def cart(request):

    return render(request,"foodapp/cart.html")

def checkout(request):

    return render(request,"foodapp/checkout.html")


class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='foodapp/signup.html'
    

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
    








