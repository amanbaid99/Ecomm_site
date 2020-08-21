from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"foodapp/home.html")

def store(request):
    return render(request,"foodapp/store.html")

def cart(request):
    return render(request,"foodapp/cart.html")

def checkout(request):
    return render(request,"foodapp/checkout.html")





