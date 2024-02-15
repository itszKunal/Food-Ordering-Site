from django.urls import path
from app import views
urlpatterns=[
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('order',views.order,name="order"),
    path('signup',views.handlesignup,name="handlesignup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
    path('contact',views.handlecontact,name="handlecontact"),
    path('payment',views.payment,name="payment"),
    path('invoice',views.invoice,name="invoice"),
]