from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store/',views.store,name='store'),
    path('login/',auth_views.LoginView.as_view(template_name='foodapp/login.html'),
                                                                    name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),


]