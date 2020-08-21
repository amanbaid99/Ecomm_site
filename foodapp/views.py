from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,"foodapp/home.html")

def store(request):
    return render(request,"foodapp/store.html")

def cart(request):
    return render(request,"foodapp/cart.html")

def checkout(request):
    return render(request,"foodapp/checkout.html")


def logout_view(request):
    logout(request)
    return render(request,'foodapp/home.html')

def login(request):
    return render(request,'foodapp/login.html')








