from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store/',views.store,name='store'),

]