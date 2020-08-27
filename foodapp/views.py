from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import forms
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from . utiils import cookieCart,cartData,guestOrder
import json
import datetime
from django.http import JsonResponse



def store(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']   
    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,"foodapp/home.html",context)

def cart(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']    
    context={'items':items,'order':order,'cartItems':cartItems}

    return render(request,"foodapp/cart.html",context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action:',action)
    print('productID:',productId)

    user=request.user
    product= Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(user=user,complete=False)

    orderItem, created =OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity=(orderItem.quantity + 1)
    elif action == 'remove' :
        orderItem.quantity =(orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
      

    return JsonResponse("Item was added",safe=False) 


def checkout(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    context={'items':items,'order':order,'cartItems':cartItems}

    return render(request,"foodapp/checkout.html",context)


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
    








