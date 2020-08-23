from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from . import forms
 from . import models


# Create your views here.

def home(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']  
    businesses= Business.objects.all()
    context={'businesses':businesses,'cartItems':cartItems}
    return render(request,"foodapp/home.html")

def store(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']  
    menus= Menu.objects.all()
    context={'menus':menus,'cartItems':cartItems}
    return render(request,"foodapp/store.html")

def cart(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    context={'items':items,'order':order,'cartItems':cartItems,'shipping':False}
    return render(request,"foodapp/cart.html")

def checkout(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']    
    context={'items':items,'order':order,'cartItems':cartItems,'shipping':False}
    return render(request,"foodapp/checkout.html")

def updateItem(request):
    data=json.loads(request.body)
    businessID=dat['businessID']
    menuID=data['menuID']
    action=data['action']
    print('action:',action)
    print('menuID:',menuID)
    print('businessID:',menuID)

    user=request.username.user
    businessID
    menu= Menu.objects.get(id=menuID)
    business= Business.objects.get(id=businessID)
    order,created=Order.objects.get_or_create(user=user,complete=False)
    orderItem, created =OrderItem.objects.get_or_create(order=order,menu=menu)

    if action == 'add':
        orderItem.quantity=(orderItem.quantity + 1)
    elif action == 'remove' :
        orderItem.quantity =(orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
      

    return JsonResponse("Item was added",safe=False) 




def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
    else:
        customer, order = guestOrder(request, data)
    total=float(data['form']['total'])
    order.transaction_id=transaction_id 

    if total == order.get_cart_total:
        order.complete=True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            
        )


    return JsonResponse('Payment complete', safe=False)

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='foodapp/signup.html'

  
class TestPage(TemplateView):
    template_name='foodapp/home.html'


class ThanksPage(TemplateView):
    success_url=reverse_lazy('login')
    template_name='foodapp/thanks.html'
    








