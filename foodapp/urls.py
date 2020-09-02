from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='foodapp/login.html'),name='login'),
    path('detail/<int:pk>/',views.detail,name='detail'),                                                          
    
                                                                    
   


]