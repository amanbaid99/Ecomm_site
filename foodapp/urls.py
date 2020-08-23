from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store/',views.store,name='store'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),


]