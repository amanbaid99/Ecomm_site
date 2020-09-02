from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import forms
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView




def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,"foodapp/home.html",context)
    
def detail(request,pk):
    products=Product.objects.get(id=pk)
    context={'products':products}

    return render(request,"foodapp/detail.html",context)

def cart(request):
    return render(request,"foodapp/cart.html")


def checkout(request):
    return render(request,"foodapp/checkout.html",)


class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='foodapp/signup.html'



class LogOutView(TemplateView):
    template_name = "foodapp/login.html"


class LogInView(TemplateView):
    template_name = "foodapp/home.html"










