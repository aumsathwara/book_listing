from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("cart/", views.cart, name="cart"),
    path("cart/cart_update", views.cart_update, name="cart_update"),
    path("search/",views.InfoListView.as_view(), name="search"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('signout/',views.signout, name="signout"),
    path("signin/home",views.home, name="home"),
]
